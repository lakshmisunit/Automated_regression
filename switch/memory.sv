module memory #(parameter WIDTH = 128, parameter DEPTH = 256)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in,
    input logic [7:0] addr,
    input logic write_en,
		input logic read_en,
    output logic [WIDTH-1:0] data_out
);
    logic [WIDTH-1:0] mem [0:DEPTH-1];

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
					for(int i=0;i<DEPTH;i++) begin
						mem[i] <= 0;
					end
        end else if (write_en) begin
            mem[addr] <= data_in;
        end
				if(read_en) begin
					data_out <= mem[addr];
				end
    end

    //assign data_out = mem[addr];
endmodule
