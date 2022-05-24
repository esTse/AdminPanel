#!/bin/sh

update_firmware() {
  local i
  local ret
  for i in $(seq 5); do
    printf "Updating firmware..."
    ret=$?
    if [ ${ret} -eq 0 ]; then
      log_msg "update_firmware in process..."
      return 0
    fi
    log_msg "update_firmware try #${i} failed... retrying."
  done
  printf "Error updating touch firmware. ${ret}"
}

log_msg() {
  logger -t "firmware-update[${PPID}]-${FLAGS_device} $@"
  echo "$@"
}

update_firmware
