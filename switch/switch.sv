module switch #(parameter WIDTH = 64, parameter PORTS = 16)(
    input logic clk,
    input logic [WIDTH-1:0] data_in,
    input logic [3:0] select,
    input logic found,
    input logic [PORTS-1:0] broadcast,
    output logic [WIDTH-1:0] data_out [PORTS-1:0]
);
    integer i;

    always_ff @(posedge clk) begin
        for (i = 0; i < PORTS; i = i + 1) begin
            data_out[i] <= {WIDTH{1'b0}};
        end

        if (found) begin
            data_out[select] <= data_in;
        end else if (broadcast) begin
            for (i = 0; i < PORTS; i = i + 1) begin
                data_out[i] <= data_in;
            end
        end
    end
endmodule
