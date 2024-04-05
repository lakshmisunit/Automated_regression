SIM_CMD := $(shell jq -r '.tools[] | select(.Simulator == "$(TOOL_NAME)") | .Simulator_CMD' settings.json)
SIM_PATH = $(shell which ${SIM_CMD})

check_simulator:
@echo ${TOOL_NAME}
	@echo ${SIM_CMD}
	@if [ -z "$(SIM_PATH)" ]; then echo "${TOOL_NAME} does not exist"; else echo "${TOOL_NAME} exists at: $(SIM_PATH)"; fi

#set compile variables


