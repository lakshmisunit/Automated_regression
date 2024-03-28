TOOL_NAME := Synopsys VCS
SIM_CMD := $(shell jq -r '.tools[] | select(.Simulator == "$(TOOL_NAME)") | .Simulator_CMD' settings.json)
SIM_PATH = $(shell which ${SIM_CMD})

check_simulator:
	@echo ${TOOL_NAME}
	@echo ${SIM_CMD}
	@if [ -z "$(SIM_PATH)" ]; then echo "${TOOL_NAME} does not exist"; else echo "${TOOL_NAME} exists at: $(SIM_PATH)"; fi




#set compile variables

SIM_CMD :=  
SIM_PATH := 
DUMP :=
TB_CMP_OPTIONS :=
INC_DIRS :=
TB_FILES :=



gen_exe_apb_base_test:
	echo ""
	echo "**** Compiling with ${SIMULATOR} ..."
	echo ""
	echo ""
	${SIM_CMD} \
	${DUMP} \
	${SIMOPTIONS} \
	${TB_CMP_OPTIONS} \
	${INC_DIRS} \
	-o gen_exe_apb_base_test \
	${TB_FILES} 2>&1 | tee ./logs/build.log

gen_exe_apb_write_verify_test:
	echo ""
	echo "**** Compiling with ${SIMULATOR}..."
	echo ""
	echo ""
	${SIM_CMD} \
	${DUMP} \
	${SIMOPTIONS} \
	${TB_CMP_OPTIONS} \
	${INC_DIRS} \
	-o gen_exe_apb_write_verify_test \
	${TB_FILES} 2>&1 | tee ./logs/build.log

gen_exe_apb_write_verify_error_test:



