----------------
-- Hello VHDL -- 
----------------

----------------
-- Example #1 --
----------------

entity cmpl_sig is
  port (
    a, b, sel : in BIT;
    x, y, z : out BIT
    );
end entity cmpl_sig;


architecture logic of cmpl_sig is
begin
  -- simple signal assignment
  x <= (a and not sel) or (b and sel);

  -- conditional signal assignment
  y <= a when sel='0' else b;

  -- selected signal assignment
  with sel select
    z <= a when '0',
         b when '1',
         0' when others;

end architecture logic;


configuration cmpl_sig_conf of cmpl_sig is
  for logic
  end for;
end configuration cmpl_sig_conf;

-----------------------------------------
-- Example #2
-- interface signal and internal signal
-----------------------------------------

entity simp is
  port (
    i1, i2 : in BIT;
    o : out BIT
    );
end entity simp;

architecture logic of simp is
  signal int : BIT;
begin
  int <=i1 and i2;
  o <= not int;
end architecture logic;
    

--------------------------------------
-- Example #3
-- use IEEE library override operator
--------------------------------------

library IEEE;
use IEEE.std_logic_1164.ALL;
use IEEE.std_logic_unsigned.ALL;

entity overload is
  port (
    a : in STD_LOGIC_VECTOR (4 downto 0);
    b : in STD_LOGIC_VECTOR (4 downto 0);
    sum : out STD_LOGIC_VECTOR (4 downto 0)
    );
end entity overload;

architecture example of overload is
begin
  sum <= a + b;
end architecture example;

-----------------------------------------
-- Example #4
-- import component structure
-----------------------------------------

entity prime is
  port (
);
end prime;

architecture prime1_arch of prime is

  component INV
    port(
      I : in STD_LOGIC;
      O : out STD_LOGIC;
      );
  end component;
  
  component AND2
    port(
      I0, I1 : in STD_LOGIC;
      O : out STD_LOGIC;
      );
  end component;

begin

  U1 : INV port map ();
  U2 : INV port map ();
  U3 : INV port map ();
  U4 : INV port map ();
  U5 : INV port map ();
  
end prime1_arch;
