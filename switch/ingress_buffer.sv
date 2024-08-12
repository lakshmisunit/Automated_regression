module ingress_buffer #(parameter WIDTH = 128, parameter PORTS = 16)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in [PORTS-1:0],
    output logic [WIDTH-1:0] data_out,
    output logic [3:0] port_num
);
    logic [WIDTH-1:0] buffer [PORTS-1:0];
    logic [3:0] read_pointer;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            read_pointer <= 4'd0;
        end else begin
					$display("entered ingress buffer");
            buffer[read_pointer] <= data_in[0];
						for(int i=0;i<PORTS;i++) begin
							$display("data_in[%0d]=%h and data_out=%h ",i, data_in[i], data_out);
						end
            //read_pointer <= read_pointer + 1;
        end
    end

    assign data_out = buffer[read_pointer];
    assign port_num = read_pointer;
endmodule
