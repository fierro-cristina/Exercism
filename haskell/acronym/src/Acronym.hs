module Acronym (abbreviate) where

import Data.Char ( toUpper, isUpper, isLower, isAlpha )

abbreviate :: String -> String
abbreviate = concatMap acronyms . words
    where
        acronyms :: String -> String
        acronyms a
            | all isUpper a = [head a]
            | all isLower a = [toUpper $ head a]
            | all (not . isAlpha) a = ""  
            | any (== '-') a = abbreviate . map (\x -> if not (isAlpha x) then ' ' else x) $ a
            | otherwise = filter isUpper a 