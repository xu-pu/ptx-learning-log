library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity or2a is
  port (
    a,b : in STD_LOGIC;
    c : out STD_LOGIC
    );
end entity or2a;

architecture behavioral of or2a is
begin
  c <= a or b;
end architecture behavioral;


entity h_subber is
  port (
    x,y : in STD_LOGIC;
    diff,s_out : out STD_LOGIC
    );
end entity h_subber;

architecture behavioral of h_subber is
  signal xyz : STD_LOGIC_VECTOR(1 downto 0);
begin
  xyz <= x & y;
  process(xyz)
    begin
      case xyz is
        when "00" =>
          diff <= "0";
          s_out <= "0";
        when "01" =>
          diff <= "1";
          s_out <= "1";
        when "10" =>
          diff <= "1";
          s_out <= "0";
        when "11" =>
          diff <= "0";
          s_out <= "0";
        when others =>
          NULL;
      end case;       
    end process;
end architecture behavioral;

entity f_subber is
  port (
    x,y,sub_in : in STD_LOGIC;
    diffr, sub_out : out STD_LOGIC
    );
end entity f_subber;

architecture behavioral of f_subber is

  component h_subber
    port (
      x,y : in STD_LOGIC;
      diff,s_out : out STD_LOGIC
      );
  end component;

  component or2a
    port (
      a,b : in STD_LOGIC;
      c : out STD_LOGIC
      );      
  end component;

  signal d,e,f : STD_LOGIC;

begin
  U1 : h_subber port map (x => x, y => y, diff => d, s_out => e);
  U2 : h_subber port map (x => d, y => sub_in, diff => diffr, s_out => f);
  U3 : or2a port map (a => f, b => e, c => sub_out);
end architecture behavioral;
