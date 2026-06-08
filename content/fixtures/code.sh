#!/usr/bin/env sh

set -eu

write_report_line() {
    section="$1"
    status="$2"
    detail="$3"

    printf '%s | %s | %s\n' "$section" "$status" "$detail"
}

write_report_line "receiving" "complete" "dock inventory matched"
write_report_line "quality" "review" "extraction fixture marker: shared code sample"
write_report_line "dispatch" "pending" "carrier window opens at 16:00"
