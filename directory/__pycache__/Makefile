ROOT := $(CURDIR)
export ROOT := $(CURDIR)
WORK_DIR := $(ROOT)/WORK_DIR

TOOL_NAME = 
SIM_CMD := $(shell jq -r '.tools[] | select(.Simulator == "$(TOOL_NAME)") | .Simulator_CMD' settings.json)
SIM_PATH = $(shell which ${SIM_CMD})


compile_files := -f $(ROOT)/regs/src/filelist.f
compile_files += -f $(ROOT)/agents/apb/src/filelist.f
compile_files += -f $(ROOT)/sequence_lib/src/filelist.f
compile_files += -f $(ROOT)/env/src/filelist.f
compile_files += -f $(ROOT)/tb/src/filelist.f
compile_files += -f $(ROOT)/src/filelist.f
 
compile_opts  :=
run_opts      := +UVM_TESTNAME=$(TEST) +UVM_TIMEOUT=10000000000 +UVM_OBJECTION_TRACE
top_module    := top
 
ifdef GUI
compile_opts  += -debug_access+r 
run_opts      += -gui
endif
 
ifdef DEBUG
run_opts      += +UVM_VERBOSITY=UVM_DEBUG 
endif
 
ifeq "$(origin dump)" "command line"
ifeq "$(dump)" "1"
DUMP         := +define+DUMP_ENABLE
else
DUMP         :=
endif
else
DUMP         := +define+DUMP_ENABLE
endif
 
# constants
vcs_compile_opts := $(compile_opts) -timescale=1ns/1ns -debug_access+r -ntb_opts uvm -sverilog -Mupdate 
vcs_run_opts     := $(run_opts)
 
# targets
vcs: run_vcs
 
check_simulator:
	@echo ${TOOL_NAME}
	@echo ${SIM_CMD}
@if [ -z "$(SIM_PATH)" ]; then echo "${TOOL_NAME} does not exist"; else echo "${TOOL_NAME} exists at: $(SIM_PATH)"; fi

prep_vcs:
	mkdir -p $(WORK_DIR) && \
	cd $(WORK_DIR) && \
	vcs 

LOG_DIR := log

#all : gen_exe_apb_write_verify_error_test gen_exe_apb_write_verify_test gen_exe_apb_base_test gen_exe_apb_random_read_write_override_test



gen_exe_apb_write_verify_error_test:
	mkdir -p $(LOG_DIR) && \
	vcs ${vcs_compile_opts} $(compile_files) -o gen_exe_apb_write_verify_error_test

gen_exe_apb_write_verify_test:
	vcs ${vcs_compile_opts} $(compile_files) -o gen_exe_apb_write_verify_test

gen_exe_apb_base_test:
	vcs ${vcs_compile_opts} $(compile_files) -o gen_exe_apb_base_test

gen_exe_apb_random_read_write_override_test:
	vcs ${vcs_compile_opts} $(compile_files) -o gen_exe_apb_random_read_write_override_test
	
run_vcs:
	${vcs_sim_exe_apb_write_verify_test}
#./simv $(vcs_run_opts) \

run_regress_scr:
	@while read -r line; do \
		if [[ "$$line" == *".log"* ]]; then \
			command="./$$line"; \
			$$command; \
		fi; \
	done < regress.scr

wave:
	cd $(WORKDIR) && \
	./simv $(vcs_run_opts) \

#coverage for individual testcase
test_coverage:
	cd $(WORK_DIR); \
	urg -dir simv.vdb -format text -report cov; \

#Merged coverage	
total_coverage:
	cd $(WORK_DIR); \
	urg -dir ./*.vdb \
	-format text \
        -parallel
 
clean_vcs:
	rm -rf $(WORK_DIR)/  
	mkdir -p $(WORK_DIR) 
