module queue #(parameter WIDTH = 8, parameter DEPTH = 16)(
    input logic clk,
    input logic reset,
    input logic [WIDTH-1:0] data_in,
    input logic enqueue,
    input logic dequeue,
    output logic [WIDTH-1:0] data_out,
    output logic empty,
    output logic full
);
    logic [WIDTH-1:0] queue_mem [0:DEPTH-1];
    logic [3:0] write_pointer, read_pointer;
    logic [3:0] count;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            write_pointer <= 4'd0;
            read_pointer <= 4'd0;
            count <= 4'd0;
        end else begin
            if (enqueue && !full) begin
                queue_mem[write_pointer] <= data_in;
                write_pointer <= write_pointer + 1;
                count <= count + 1;
            end
            if (dequeue && !empty) begin
                data_out <= queue_mem[read_pointer];
                read_pointer <= read_pointer + 1;
                count <= count - 1;
            end
        end
    end

    assign empty = (count == 0);
    assign full = (count == DEPTH);
endmodule
