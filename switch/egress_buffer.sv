module egress_buffer #(parameter WIDTH = 128)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in,
    output logic [WIDTH-1:0] data_out
);
    logic [WIDTH-1:0] buffer;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            buffer <= {WIDTH{1'b0}};
        end else begin
            buffer <= data_in;
        end
    end

    assign data_out = buffer;
endmodule
