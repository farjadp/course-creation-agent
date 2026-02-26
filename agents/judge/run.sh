#!/bin/bash
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd "${SCRIPT_DIR}"

if [[ "${PORT}" == "" ]]; then
    PORT="8080"
fi

python3 adk_app.py --host "0.0.0.0" --port ${PORT} \
    --trace_to_cloud \
    --a2a \
    .
