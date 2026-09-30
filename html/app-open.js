// Separate SparkOS app-opening animation controller.
function openSparkApp(element){if(!element)return;element.classList.remove('spark-app-window');void element.offsetWidth;element.classList.add('spark-app-window')}
window.openSparkApp=openSparkApp;
