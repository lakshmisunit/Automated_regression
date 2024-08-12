module tb_network_switch;

    parameter WIDTH = 128;
    parameter PORTS = 16;
    parameter QUEUE_DEPTH = 16;

    logic clk;
    logic reset;

    logic [WIDTH-1:0] data_in [PORTS-1:0];
    logic [WIDTH-1:0] data_out [PORTS-1:0];

    network_switch #(WIDTH, PORTS, QUEUE_DEPTH) uut (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(data_out)
    );

    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    initial begin
        reset = 1;
        #15;
        reset = 0;
    end

    task init_data;
        input [WIDTH-1:0] data;
        integer i;
        begin
            for (i = 0; i < PORTS; i = i + 1) begin
                data_in[i] = data;
            end
        end
    endtask

    task check_output;
        input [WIDTH-1:0] expected_data [PORTS-1:0];
        integer i;
        begin
            for (i = 0; i < PORTS; i = i + 1) begin
                if (data_out[i] !== expected_data[i]) begin
                    $display("Mismatch at port %0d: expected %h, got %h", i, expected_data[i], data_out[i]);
                end
            end
        end
    endtask

    task fill_expected_data;
        input [WIDTH-1:0] value;
        output [WIDTH-1:0] expected_data [PORTS-1:0];
        integer i;
        begin
            for (i = 0; i < PORTS; i = i + 1) begin
                expected_data[i] = value;
            end
        end
    endtask

    task test_basic_forwarding;
        reg [WIDTH-1:0] expected_data [PORTS-1:0];
        begin
            $display("Running Basic Forwarding Test");
            //init_data(128'b0);
            data_in[4] = 128'h23456789ABCDEF0AABBCC112233445566;
            #10;
            fill_expected_data(128'h23456789ABCDEF0AABBCC11223344565, expected_data);
            check_output(expected_data);
        end
    endtask

    task test_mac_table_update;
        reg [WIDTH-1:0] expected_data [PORTS-1:0];
        begin
            $display("Running MAC Table Update Test");
            //init_data(128'b0);
            data_in[4] = 128'h332211AA112233445566AABBCCDDEEFF;
            #10;
            fill_expected_data(128'h332211AABBCCDDEEFF00112233445566, expected_data);
            check_output(expected_data);
        end
    endtask

    task test_broadcast;
        reg [WIDTH-1:0] expected_data [PORTS-1:0];
        begin
            $display("Running Broadcast Test");
            //init_data(64'b0);
            data_in[0] = 128'hFFFFFFFF112233445566AABBCCDDEEFF;
            #10;
            fill_expected_data(128'hFFFFFFFFFFFFFFFFFFFF000000000000, expected_data);
            check_output(expected_data);
        end
    endtask

    task test_queue_operations;
        reg [WIDTH-1:0] expected_data [PORTS-1:0];
        begin
            $display("Running Queue Operations Test");
            //init_data(128'b0);
            data_in[4] = 128'h01112233112233445566AABBCCDDEEFF;
            #10;
            fill_expected_data(128'h0011122334455667788aabcdeffecdba, expected_data);
            check_output(expected_data);
        end
    endtask

    initial begin
			repeat(100) begin
        test_basic_forwarding;
        test_mac_table_update;
        test_broadcast;
        test_queue_operations;
			end
			
        $finish;
    end

endmodule
