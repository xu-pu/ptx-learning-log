library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity 2to4_codec is
  port (
    I0, I1, EN : in STD_LOGIC;
    Y0, Y1, Y2, Y3 : out STD_LOGIC
    );
end entity 2to4_codec;

architecture codec of 2to4_codec is
  
