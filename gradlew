#!/bin/bash
pushd admin
./gradlew "$@"
popd
