library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.NUMERIC_STD.ALL;

-- D flip-flop from wiki

entity D_FF is
  port (
    clock : in STD_LOGIC;
    reset : in STD_LOGIC
    pre : in STD_LOGIC;
    ce : in STD_LOGIC;
    d : in STD_LOGIC;
    q : in STD_LOGIC
    );
end entity D_FF;

architecture behavioral of D_FF is
begin
  process(clock) is
  begin
    if rising_edge(clock) then
      if (reset='1') then
        q <= '0';
      elsif (pre='1') then
        q <= '1';
      elsif (ce='1') then
        q <= d;
      end if;
    end if;
  end process;
end architecture behavioral;

-- T flip-flop

entity T_FF is
  port (
    T : in STD_LOGIC;
    reset : in STD_LOGIC;
    clock_enable : in STD_LOGIC;
    clock : in STD_LOGIC;
    output : out STD_LOGIC
    );
end entity T_FF;

architecture behavioral of T_FF is
  signal temp : STD_LOGIC;
begin
  process(clock)
  begin
    if clock'event and clock='1' then
      if reset='1' then
        temp <= '0';
      elsif clock_enable='1' then
        if T='0' then
          temp <= temp;
        elsif T='1' then
          temp <= not (temp);
        end if;
      end if;
    end if;
  end process;
  output  <= temp;
end behavioral;

-- J-K flip-flop -- form wiki

entity JK_FF is
  port (
    J, K : in STD_LOGIC;
    reset : in STD_LOGIC;
    clock_enable : in STD_LOGIC;
    clock : in STD_LOGIC;
    output : out STD_LOGIC
    );
end JK_FF;

architecture behavioral of JK_FF is
  signal temp : STD_LOGIC;
begin:
     process(clock)
     begin
         if (clock'event and clock='1') then
           temp <= '0';
         elsif clock_enable='0' then
           if (J='0' and K='0') then
             temp <= temp;
           elsif (J='0' and K='1') then
             temp <= '0';
           elsif (J='1' and K='0') then
             temp <= '1';
           elsif (J='1' and K='1') then
             temp <= not (temp);             
           end if;
         end if;
     end process;
     output <= temp;
end behavioral;

-- 4-bit ALU -- wiki

entity ALU is
  port (
    nibble1, nibble2 : in STD_LOGIC_VECTOR(3 downto 0);
    operation : in STD_LOGIC_VECTOR(2 downto 0);
    carry_out : out STD_LOGIC;
    flag : out STD_LOGIC;
    result : STD_LOGIC_VECTOR(3 downto 0)
    );
end entity ALU;

architecture behavioral of ALU is
  signal temp : STD_LOGIC_VECTOR(4 downto 0);
begin
  flag <= '0';
  case operation is
    when '000' =>
      temp <= STD_LOGIC_VECTOR((unsigned("0" & nibble1)+unsigned(nibble2)));
      result <= temp(3 downto 0);
      carry_out <= temp(4);
    when '001' =>
      if (nibble1 >= nibble2) then
        temp <= STD_LOGIC_VECTOR(unsigned(nibble1) - unsigned(nibble2));
        flag <= '0';
      else
        temp <= STD_LOGIC_VECTOR(unsigned(nibble2) - unsigned(nibble1));
        flag <= '1';
      end if;
    when '010' =>
      result <= nibble1 and nibble2;
    when '011' =>
      result <= nibble1 or nibble2;
    when '100' =>
      result <= nibble1 xor nibble2;      
    when '101' =>
      result <= not nibble1;
    when '110' =>
      result <= not nibble2;
    when others =>
      temp <= STD_LOGIC_VECTOR((unsigned("0" & nibble1) + unsigned(not nibble2)) + 1);
      result <= temp(3 downto 0);
      flag <= temp(4);
    end case;
  end process      
end architecture behavioral;
