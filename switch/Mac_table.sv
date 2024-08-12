module mac_table #(parameter ADDR_WIDTH = 48, parameter PORTS = 16)(
    input logic clk,
    input logic reset,
    input logic [ADDR_WIDTH-1:0] mac_addr_in,
    input logic [ADDR_WIDTH-1:0] src_addr_in,
    input logic [3:0] incoming_port,
    output logic [3:0] port_out,
    output logic found,
    output logic [PORTS-1:0] broadcast
);
    typedef struct {
        logic [ADDR_WIDTH-1:0] mac_addr;
        logic [3:0] port;
    } mac_entry_t;

    mac_entry_t mac_table [0:PORTS-1];
    integer i;

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            found <= 1'b0;
            port_out <= 4'd0;
            broadcast <= {PORTS{1'b1}};
            for (i = 0; i < PORTS; i = i + 1) begin
                mac_table[i].mac_addr <= {ADDR_WIDTH{1'b0}};
                mac_table[i].port <= 4'd0;
            end
        end else begin
            found <= 1'b0;
            broadcast <= {PORTS{1'b0}};
            for (i = 0; i < PORTS; i = i + 1) begin
                if (mac_table[i].mac_addr == mac_addr_in) begin
                    found <= 1'b1;
										$write("mac_addr_in = %h", mac_addr_in);
                    port_out <= mac_table[i].port;
                    break;
                end
            end
            if (!found) begin
                broadcast <= {PORTS{1'b1}};
                for (i = 0; i < PORTS; i = i + 1) begin
                    if (mac_table[i].mac_addr == {ADDR_WIDTH{1'b0}}) begin
                        mac_table[i].mac_addr <= src_addr_in;
                        mac_table[i].port <= incoming_port;
												$write("src_addr_in = %h", src_addr_in);
                        break;
                    end
                end
            end
        end
    end
endmodule
