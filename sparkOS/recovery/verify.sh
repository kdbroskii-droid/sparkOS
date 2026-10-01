#!/bin/sh
set -eu
ROOT=${SPARK_RECOVERY_ROOT:-/run/sparkos-recovery}
MANIFEST="$ROOT/manifest.sha256"
[ -f "$MANIFEST" ] || { echo "RECOVERY_VERIFY_FAILED: manifest missing";exit 1; }
if (cd "$ROOT" && sha256sum -c "$MANIFEST" --quiet);then echo "RECOVERY_VERIFY_OK";else echo "RECOVERY_VERIFY_FAILED";exit 1;fi
