//! Small, dependency-free input binding and application routing core for SparkOS.
//!
//! This module deliberately does not spawn host processes. The future SparkOS
//! window manager/session manager must implement `ShellActions` and connect it
//! to native process, window, and input services. Keeping this core small avoids
//! a permanently running helper process and makes the routing logic testable.

use std::collections::BTreeMap;

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord)]
pub enum Key {
    A, B, C, D, E, F, I, L, M, N, Q, R, S, T, W,
    Digit1, Digit2, Digit3, Digit4, Digit5, Digit6, Digit7, Digit8, Digit9,
    Tab, Enter, Escape, Space, F4, F5, F11, Left, Right, Up, Down,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Default)]
pub struct Modifiers {
    pub super_key: bool,
    pub ctrl: bool,
    pub alt: bool,
    pub shift: bool,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct KeyStroke {
    pub key: Key,
    pub modifiers: Modifiers,
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum MouseButton { Left, Right, Middle, Back, Forward }

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Action {
    OpenLauncher,
    OpenApp(&'static str),
    OpenNextPinnedApp(u8),
    CloseFocusedWindow,
    SwitchWindow,
    ToggleMaximize,
    FocusNextWorkspace,
    FocusPreviousWorkspace,
    ShowDesktop,
    OpenQuickSettings,
    OpenNotifications,
    OpenTaskView,
    GoBack,
    GoForward,
    ActivatePointerTarget,
    ShowContextMenu,
    ScrollVertical(i8),
    ScrollHorizontal(i8),
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum InputEvent {
    KeyDown(KeyStroke),
    MouseDown(MouseButton),
    Wheel { vertical: i8, horizontal: i8 },
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Binding {
    pub stroke: KeyStroke,
    pub action: Action,
}

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum DispatchError {
    UnknownApp(&'static str),
    ActionFailed(&'static str),
}

/// Implement this at the OS/session-manager boundary. App IDs are stable IDs,
/// never shell command strings, so key presses cannot inject arbitrary commands.
pub trait ShellActions {
    fn open_launcher(&mut self) -> Result<(), DispatchError>;
    fn launch_app(&mut self, app_id: &'static str) -> Result<(), DispatchError>;
    fn launch_pinned_app(&mut self, slot: u8) -> Result<(), DispatchError>;
    fn close_focused_window(&mut self) -> Result<(), DispatchError>;
    fn switch_window(&mut self) -> Result<(), DispatchError>;
    fn toggle_maximize(&mut self) -> Result<(), DispatchError>;
    fn change_workspace(&mut self, direction: i8) -> Result<(), DispatchError>;
    fn show_desktop(&mut self) -> Result<(), DispatchError>;
    fn open_quick_settings(&mut self) -> Result<(), DispatchError>;
    fn open_notifications(&mut self) -> Result<(), DispatchError>;
    fn open_task_view(&mut self) -> Result<(), DispatchError>;
    fn navigate_history(&mut self, direction: i8) -> Result<(), DispatchError>;
    fn activate_pointer_target(&mut self) -> Result<(), DispatchError>;
    fn show_context_menu(&mut self) -> Result<(), DispatchError>;
    fn scroll(&mut self, vertical: i8, horizontal: i8) -> Result<(), DispatchError>;
}

fn mods(super_key: bool, ctrl: bool, alt: bool, shift: bool) -> Modifiers {
    Modifiers { super_key, ctrl, alt, shift }
}
fn stroke(key: Key, m: Modifiers) -> KeyStroke { KeyStroke { key, modifiers: m } }

/// Built-in bindings. Users should be able to override these later in Settings.
pub fn default_bindings() -> BTreeMap<KeyStroke, Action> {
    let mut b = BTreeMap::new();
    let super_only = mods(true, false, false, false);
    let super_shift = mods(true, false, false, true);
    let super_alt = mods(true, false, true, false);
    let alt = mods(false, false, true, false);
    let none = mods(false, false, false, false);

    b.insert(stroke(Key::Space, super_only), Action::OpenLauncher);
    b.insert(stroke(Key::E, super_only), Action::OpenApp("files"));
    b.insert(stroke(Key::C, super_only), Action::OpenApp("chrome"));
    b.insert(stroke(Key::S, super_only), Action::OpenApp("settings"));
    b.insert(stroke(Key::I, super_only), Action::OpenApp("spark-ai"));
    b.insert(stroke(Key::T, super_only), Action::OpenApp("terminal"));
    b.insert(stroke(Key::Q, super_only), Action::OpenQuickSettings);
    b.insert(stroke(Key::N, super_only), Action::OpenNotifications);
    b.insert(stroke(Key::Tab, super_only), Action::OpenTaskView);
    b.insert(stroke(Key::D, super_only), Action::ShowDesktop);
    b.insert(stroke(Key::F4, alt), Action::CloseFocusedWindow);
    b.insert(stroke(Key::Tab, alt), Action::SwitchWindow);
    b.insert(stroke(Key::F11, none), Action::ToggleMaximize);
    b.insert(stroke(Key::Left, super_only), Action::FocusPreviousWorkspace);
    b.insert(stroke(Key::Right, super_only), Action::FocusNextWorkspace);
    b.insert(stroke(Key::Left, super_shift), Action::FocusPreviousWorkspace);
    b.insert(stroke(Key::Right, super_shift), Action::FocusNextWorkspace);
    b.insert(stroke(Key::Left, super_alt), Action::GoBack);
    b.insert(stroke(Key::Right, super_alt), Action::GoForward);

    for (key, slot) in [
        (Key::Digit1, 1), (Key::Digit2, 2), (Key::Digit3, 3),
        (Key::Digit4, 4), (Key::Digit5, 5), (Key::Digit6, 6),
        (Key::Digit7, 7), (Key::Digit8, 8), (Key::Digit9, 9),
    ] {
        b.insert(stroke(key, super_only), Action::OpenNextPinnedApp(slot));
    }
    b
}

/// Dispatches one event. Returns false when no binding handled the event.
pub fn dispatch<A: ShellActions>(
    event: InputEvent,
    bindings: &BTreeMap<KeyStroke, Action>,
    shell: &mut A,
) -> Result<bool, DispatchError> {
    match event {
        InputEvent::KeyDown(key) => {
            let Some(action) = bindings.get(&key).copied() else { return Ok(false) };
            match action {
                Action::OpenLauncher => shell.open_launcher()?,
                Action::OpenApp(id) => shell.launch_app(id)?,
                Action::OpenNextPinnedApp(slot) => shell.launch_pinned_app(slot)?,
                Action::CloseFocusedWindow => shell.close_focused_window()?,
                Action::SwitchWindow => shell.switch_window()?,
                Action::ToggleMaximize => shell.toggle_maximize()?,
                Action::FocusNextWorkspace => shell.change_workspace(1)?,
                Action::FocusPreviousWorkspace => shell.change_workspace(-1)?,
                Action::ShowDesktop => shell.show_desktop()?,
                Action::OpenQuickSettings => shell.open_quick_settings()?,
                Action::OpenNotifications => shell.open_notifications()?,
                Action::OpenTaskView => shell.open_task_view()?,
                Action::GoBack => shell.navigate_history(-1)?,
                Action::GoForward => shell.navigate_history(1)?,
                Action::ActivatePointerTarget => shell.activate_pointer_target()?,
                Action::ShowContextMenu => shell.show_context_menu()?,
                Action::ScrollVertical(v) => shell.scroll(v, 0)?,
                Action::ScrollHorizontal(h) => shell.scroll(0, h)?,
            }
            Ok(true)
        }
        InputEvent::MouseDown(MouseButton::Left) => {
            shell.activate_pointer_target()?;
            Ok(true)
        }
        InputEvent::MouseDown(MouseButton::Right) => {
            shell.show_context_menu()?;
            Ok(true)
        }
        InputEvent::MouseDown(MouseButton::Middle) => Ok(false),
        InputEvent::MouseDown(MouseButton::Back) => {
            shell.navigate_history(-1)?;
            Ok(true)
        }
        InputEvent::MouseDown(MouseButton::Forward) => {
            shell.navigate_history(1)?;
            Ok(true)
        }
        InputEvent::Wheel { vertical, horizontal } => {
            shell.scroll(vertical, horizontal)?;
            Ok(true)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[derive(Default)]
    struct FakeShell { calls: Vec<String> }
    impl ShellActions for FakeShell {
        fn open_launcher(&mut self)->Result<(),DispatchError>{self.calls.push("launcher".into());Ok(())}
        fn launch_app(&mut self,id:&'static str)->Result<(),DispatchError>{self.calls.push(format!("app:{id}"));Ok(())}
        fn launch_pinned_app(&mut self,n:u8)->Result<(),DispatchError>{self.calls.push(format!("pin:{n}"));Ok(())}
        fn close_focused_window(&mut self)->Result<(),DispatchError>{self.calls.push("close".into());Ok(())}
        fn switch_window(&mut self)->Result<(),DispatchError>{self.calls.push("switch".into());Ok(())}
        fn toggle_maximize(&mut self)->Result<(),DispatchError>{self.calls.push("maximize".into());Ok(())}
        fn change_workspace(&mut self,n:i8)->Result<(),DispatchError>{self.calls.push(format!("workspace:{n}"));Ok(())}
        fn show_desktop(&mut self)->Result<(),DispatchError>{self.calls.push("desktop".into());Ok(())}
        fn open_quick_settings(&mut self)->Result<(),DispatchError>{self.calls.push("quick".into());Ok(())}
        fn open_notifications(&mut self)->Result<(),DispatchError>{self.calls.push("notifications".into());Ok(())}
        fn open_task_view(&mut self)->Result<(),DispatchError>{self.calls.push("taskview".into());Ok(())}
        fn navigate_history(&mut self,n:i8)->Result<(),DispatchError>{self.calls.push(format!("history:{n}"));Ok(())}
        fn activate_pointer_target(&mut self)->Result<(),DispatchError>{self.calls.push("activate".into());Ok(())}
        fn show_context_menu(&mut self)->Result<(),DispatchError>{self.calls.push("context".into());Ok(())}
        fn scroll(&mut self,v:i8,h:i8)->Result<(),DispatchError>{self.calls.push(format!("scroll:{v}:{h}"));Ok(())}
    }

    #[test]
    fn search_c_launches_chrome_by_id() {
        let mut shell = FakeShell::default();
        let handled = dispatch(
            InputEvent::KeyDown(stroke(Key::C, mods(true,false,false,false))),
            &default_bindings(), &mut shell
        ).unwrap();
        assert!(handled);
        assert_eq!(shell.calls, vec!["app:chrome"]);
    }

    #[test]
    fn super_e_launches_files_by_id() {
        let mut shell = FakeShell::default();
        let handled = dispatch(
            InputEvent::KeyDown(stroke(Key::E, mods(true,false,false,false))),
            &default_bindings(), &mut shell
        ).unwrap();
        assert!(handled);
        assert_eq!(shell.calls, vec!["app:files"]);
    }

    #[test]
    fn alt_f4_closes_focused_window() {
        let mut shell = FakeShell::default();
        dispatch(
            InputEvent::KeyDown(stroke(Key::F4, mods(false,false,true,false))),
            &default_bindings(), &mut shell
        ).unwrap();
        assert_eq!(shell.calls, vec!["close"]);
    }

    #[test]
    fn unknown_key_is_not_consumed() {
        let mut shell = FakeShell::default();
        let handled = dispatch(
            InputEvent::KeyDown(stroke(Key::A, mods(false,false,false,false))),
            &default_bindings(), &mut shell
        ).unwrap();
        assert!(!handled);
        assert!(shell.calls.is_empty());
    }

    #[test]
    fn mouse_buttons_route_to_shell() {
        let mut shell = FakeShell::default();
        dispatch(InputEvent::MouseDown(MouseButton::Left), &default_bindings(), &mut shell).unwrap();
        dispatch(InputEvent::MouseDown(MouseButton::Right), &default_bindings(), &mut shell).unwrap();
        assert_eq!(shell.calls, vec!["activate", "context"]);
    }
}
