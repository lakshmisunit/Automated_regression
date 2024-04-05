MAKEFLAGS += --silent
ROOT := $(CURDIR)
export ROOT := $(CURDIR)
file := 
Simulator_cmd :=
compile_opts :=
compile_files := -f $(ROOT)/regs/src/filelist.f
compile_files += -f $(ROOT)/agents/apb/src/filelist.f
compile_files += -f $(ROOT)/sequence_lib/src/filelist.f
compile_files += -f $(ROOT)/env/src/filelist.f
compile_files += -f $(ROOT)/tb/src/filelist.f
compile_files += -f $(ROOT)/src/filelist.f
output_file :=

	
build:
	if [ -e ${output_file} ]; then \
		${MAKE} clean; \
	else \
	  echo "no such file or directory"; \
		echo "but it is here"; \
	fi
 
gen_exe_apb_write_verify_test: 
	${Simulator_CMD} ${compile_opts} ${compile_files} -o ${output_file}

gen_exe_apb_write_verify_error_test:
	${Simulator_CMD} ${compile_opts} ${compile_files} -o ${output_file}

gen_exe_apb_base_test:
	${Simulator_CMD} ${compile_opts} ${compile_files} -o ${output_file}

gen_exe_apb_random_read_write_override_test:
	${Simulator_CMD} ${compile_opts} ${compile_files} -o ${output_file}

	
