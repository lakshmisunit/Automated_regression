module network_switch #(parameter WIDTH = 128, parameter PORTS = 16, parameter QUEUE_DEPTH = 16)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in [PORTS-1:0],
    output logic [WIDTH-1:0] data_out [PORTS-1:0]
);
    logic [WIDTH-1:0] ingress_data;
    logic [3:0] incoming_port;
    logic [47:0] src_addr;
    logic [47:0] dst_addr;
    logic [3:0] port_select;
    logic found;
    logic [PORTS-1:0] broadcast;
    logic [WIDTH-1:0] memory_data_out;
    logic [7:0] memory_addr;
    logic memory_write_en;
		logic memory_read_en;
		logic [7:0] next_free_memory_addr;
    logic [127:0] egress_data;
    logic [127:0] queues_data_out [PORTS-1:0];
    logic [PORTS-1:0] queue_enqueue;
    logic [PORTS-1:0] queue_dequeue;
    logic [PORTS-1:0] queue_empty;
    logic [PORTS-1:0] queue_full;

    ingress_buffer #(WIDTH, PORTS) ingress_buffer_inst (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(ingress_data)
        //.port_num(incoming_port)
    );

    memory #(WIDTH, 256) memory_inst (
        .clk(clk),
        .reset(reset),
        .data_in(ingress_data),
        .addr(memory_addr),
        .write_en(1),
				.read_en(memory_read_en),
        .data_out(memory_data_out)
    );

    egress_buffer #(WIDTH) egress_buffer_inst (
        .clk(clk),
        .reset(reset),
        .data_in(memory_data_out),
        .data_out(egress_data)
    );

    mac_table #(48, PORTS) mac_table_inst (
        .clk(clk),
        .reset(reset),
        .mac_addr_in(dst_addr),
        .src_addr_in(src_addr),
        .incoming_port(incoming_port),
        .port_out(port_select),
        .found(found),
        .broadcast(broadcast)
    );

    switch #(WIDTH, PORTS) switch_inst (
        .clk(clk),
        .data_in(egress_data),
        .select(port_select),
        .found(found),
        .broadcast(broadcast),
        .data_out(queues_data_out)
    );

    genvar i;
    generate
        for (i = 0; i < PORTS; i = i + 1) begin: queue_gen
            queue #(WIDTH, QUEUE_DEPTH) queue_inst (
                .clk(clk),
                .reset(reset),
                .data_in(memory_addr),
                .enqueue(queue_enqueue[i]),
                .dequeue(queue_dequeue[i]),
                .data_out(data_out[i]),
                .empty(queue_empty[i]),
                .full(queue_full[i])
            );
        end
    endgenerate

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            queue_enqueue <= {PORTS{1'b0}};
            queue_dequeue <= {PORTS{1'b0}};
						next_free_memory_addr <= '0;
        end else begin
					for(int i=0;i<PORTS;i++) begin
						if(data_in[i] !== '0) begin
							incoming_port = i;
							src_addr = data_in[i][47:0];
							dst_addr = data_in[i][95:48];
						end
					end
					memory_addr = next_free_memory_addr;
					memory_write_en <= 1;
					memory_read_en <= 1;
					next_free_memory_addr <= next_free_memory_addr + 1;
					//src_addr = data_in[0][47:0];
					//dst_addr = data_in[0][95:48];
					$write("src_addr = %h", data_in[0][47:0]);
            queue_enqueue <= {PORTS{1'b0}};
            queue_dequeue <= {PORTS{1'b0}};
						if(!broadcast) begin

							memory_read_en <= 1;
							queue_dequeue <= {PORTS{1'b1}};
						end
            if (found) begin
							$display("queue_enqueue[%d] = %d", port_select, 1); 
                queue_enqueue[port_select] <= 1'b1;
								memory_read_en <= 1;
            end else if (broadcast) begin
                queue_enqueue <= {PORTS{1'b1}};
            end
        end
    end
endmodule


/*module network_switch #(parameter WIDTH = 128, parameter PORTS = 16, parameter QUEUE_DEPTH = 16, parameter MEM_SIZE = 256)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in [PORTS-1:0],
    output logic [WIDTH-1:0] data_out [PORTS-1:0]
);
    logic [WIDTH-1:0] ingress_data;
    logic [3:0] incoming_port;
    logic [47:0] src_addr;
    logic [47:0] dst_addr;
    logic [3:0] port_select;
    logic found;
    logic [PORTS-1:0] broadcast;
    logic [WIDTH-1:0] memory_data_out;
    logic [7:0] memory_addr;
    logic memory_write_en;
    logic [7:0] memory_addr_out [PORTS-1:0];
    logic [WIDTH-1:0] egress_data;
    logic [PORTS-1:0] queue_enqueue;
    logic [PORTS-1:0] queue_dequeue;
    logic [PORTS-1:0] queue_empty;
    logic [PORTS-1:0] queue_full;
    logic [7:0] next_free_memory_addr;
    logic [7:0] addr_to_push [PORTS-1:0];
    logic [7:0] allocated_memory_addr;
    logic [PORTS-1:0] address_valid;

    initial begin
        next_free_memory_addr = 8'h0;
    end

    ingress_buffer #(WIDTH, PORTS) ingress_buffer_inst (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(ingress_data),
        .port_num(incoming_port)
    );

    memory #(WIDTH, MEM_SIZE) memory_inst (
        .clk(clk),
        .reset(reset),
        .data_in(ingress_data),
        .addr(memory_addr),
        .write_en(memory_write_en),
        .data_out(memory_data_out)
    );

    egress_buffer #(WIDTH) egress_buffer_inst (
        .clk(clk),
        .reset(reset),
        .data_in(memory_data_out),
        .data_out(data_out[incoming_port])
    );

    mac_table #(48, PORTS) mac_table_inst (
        .clk(clk),
        .reset(reset),
        .mac_addr_in(dst_addr),
        .src_addr_in(src_addr),
        .incoming_port(incoming_port),
        .port_out(port_select),
        .found(found),
        .broadcast(broadcast)
    );

    switch #(WIDTH, PORTS) switch_inst (
        .clk(clk),
        .data_in(egress_data),
        .select(port_select),
        .found(found),
        .broadcast(broadcast),
        .data_out(memory_addr_out)
    );

    genvar i;
    generate
        for (i = 0; i < PORTS; i = i + 1) begin: queue_gen
            queue #(8, QUEUE_DEPTH) queue_inst (
                .clk(clk),
                .reset(reset),
                .data_in(memory_addr_out[i]),
                .enqueue(queue_enqueue[i]),
                .dequeue(queue_dequeue[i]),
                .data_out(addr_to_push[i]),
                .empty(queue_empty[i]),
                .full(queue_full[i])
            );
        end
    endgenerate

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            incoming_port <= 0;
            src_addr <= '0;
            dst_addr <= '0;
            queue_enqueue <= {PORTS{1'b0}};
            queue_dequeue <= {PORTS{1'b0}};
            memory_write_en <= 0;
            next_free_memory_addr <= 8'h0;
            allocated_memory_addr <= 8'h0;
            address_valid <= {PORTS{1'b0}};
        end else begin
            incoming_port <= '0;
            for (int i = 0; i < PORTS; i++) begin
                if (data_in[i] !== '0) begin
                    incoming_port <= i;
                    ingress_data <= data_in[i];
                    src_addr <= ingress_data[47:0];
                    dst_addr <= ingress_data[95:48];
                    $write("src_addr = %h\n", src_addr);
                end
            end

            memory_write_en <= 1;
            memory_addr <= next_free_memory_addr;
            allocated_memory_addr <= next_free_memory_addr;

            next_free_memory_addr <= next_free_memory_addr + 1;

            if (found) begin
                queue_enqueue[port_select] <= 1'b1;
                address_valid[port_select] <= 1'b1;
            end else if (broadcast) begin
                queue_enqueue <= {PORTS{1'b1}};
                address_valid <= {PORTS{1'b1}};
            end

            for (int j = 0; j < PORTS; j++) begin
                if (queue_dequeue[j] && !queue_empty[j] && address_valid[j]) begin
                    memory_addr_out[j] <= allocated_memory_addr;
                end
            end
        end
    end

endmodule*/

/*module network_switch #(parameter WIDTH = 128, parameter PORTS = 16, parameter QUEUE_DEPTH = 16, parameter MEM_SIZE = 256)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in [PORTS-1:0],
    output logic [WIDTH-1:0] data_out [PORTS-1:0]
);

    logic [WIDTH-1:0] ingress_data;
    logic [3:0] incoming_port;
    logic [47:0] src_addr;
    logic [47:0] dst_addr;
    logic [3:0] port_select;
    logic found;
    logic broadcast;
    logic [7:0] next_free_memory_addr;
    logic [PORTS-1:0] queue_enqueue;
    logic [PORTS-1:0] queue_dequeue;
    logic [PORTS-1:0] queue_empty;
    logic [PORTS-1:0] queue_full;
    logic [WIDTH-1:0] memory_data_out;
    logic [7:0] queue_addr_out [PORTS-1:0];
    logic [PORTS-1:0] address_valid;

    ingress_buffer #(WIDTH, PORTS) ingress_buffer_inst (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(ingress_data)
        //.port_num(incoming_port)
    );

    memory #(WIDTH, MEM_SIZE) memory_inst (
        .clk(clk),
        .reset(reset),
        .data_in(ingress_data),
        .addr(next_free_memory_addr),
        .write_en(1'b1),
        .data_out(memory_data_out)
    );

    mac_table #(48, PORTS) mac_table_inst (
        .clk(clk),
        .reset(reset),
        .mac_addr_in(dst_addr),
        .src_addr_in(src_addr),
        .incoming_port(incoming_port),
        .port_out(port_select),
        .found(found),
        .broadcast(broadcast)
    );

    genvar i;
    generate
        for (i = 0; i < PORTS; i = i + 1) begin: queue_gen
            queue #(8, QUEUE_DEPTH) queue_inst (
                .clk(clk),
                .reset(reset),
                .data_in(next_free_memory_addr),
                .enqueue(queue_enqueue[i]),
                .dequeue(queue_dequeue[i]),
                .data_out(queue_addr_out[i]),
                .empty(queue_empty[i]),
                .full(queue_full[i])
            );
        end
    endgenerate

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            incoming_port <= 0;
            src_addr <= '0;
            dst_addr <= '0;
            queue_enqueue <= {PORTS{1'b0}};
            queue_dequeue <= {PORTS{1'b0}};
            next_free_memory_addr <= 8'h0;
            address_valid <= {PORTS{1'b0}};
        end else begin
            for (int i = 0; i < PORTS; i++) begin
                if (data_in[i] !== '0) begin
                    incoming_port <= i;
                    //ingress_data <= data_in[i];
                    src_addr <= ingress_data[47:0];
                    dst_addr <= ingress_data[95:48];
                end
            end

            if (found) begin
                queue_enqueue[port_select] <= 1'b1;
                address_valid[port_select] <= 1'b1;
            end else if (broadcast) begin
                queue_enqueue <= {PORTS{1'b1}};
                address_valid <= {PORTS{1'b1}};
            end

            for (int j = 0; j < PORTS; j++) begin
                if (!queue_empty[j] && address_valid[j]) begin
                    queue_dequeue[j] <= 1'b1;
                    data_out[j] <= memory_data_out;
                end else begin
                    queue_dequeue[j] <= 1'b0;
                    data_out[j] <= '0;
                end
            end

            next_free_memory_addr <= next_free_memory_addr + 1;
        end
    end

endmodule*/
