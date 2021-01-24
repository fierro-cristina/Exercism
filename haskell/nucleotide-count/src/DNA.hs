module DNA (nucleotideCounts, Nucleotide(..)) where

import Data.Map (Map, adjust, fromList)
import Control.Monad ( foldM )

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

processNucleotides :: Char -> Either String Nucleotide
processNucleotides n = case n of
    'A' -> Right A
    'T' -> Right T
    'C' -> Right C
    'G' -> Right G
    _   -> Left "Sequence is invalid!" 

nucleotideCounts :: String -> Either String (Map Nucleotide Int)
nucleotideCounts = foldM go blank
        where go nmap x = (\c -> adjust (+1) c nmap) <$> processNucleotides x
              blank = fromList [(A, 0), (C, 0), (G, 0), (T, 0)]




