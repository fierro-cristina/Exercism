module Bob (responseFor) where

import Data.Char ( isAlpha, isUpper, isSpace )
import Data.List ( dropWhileEnd )


responseFor :: String -> String
responseFor xs
    | isYelling = "Whoa, chill out!"
    | isQuestion = "Sure."
    | isYellingQuestion = "Calm down, I know what I'm doing!"
    | isSilent = " Fine. Be that way!"
    | otherwise  = "Whatever."

    where strippedInput = stripInput xs

        isYelling = all isUpper strippedInput
        isQuestion = last strippedInput  == '?'
        isYellingQuestion = isYelling && isQuestion        
        isSilent = all isSpace strippedInput

stripInput :: String -> String 
stripInput s = dropWhileEnd isSpace (dropWhile isSpace s)