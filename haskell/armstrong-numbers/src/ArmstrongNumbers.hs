module ArmstrongNumbers (armstrong) where

import Data.Char( digitToInt)

armstrong :: Integral a => a -> Bool
armstrong a = sumAllToPower == toInteger a
    where
        digitsToInt = map digitToInt . show $ toInteger a
        nOfDigits = length digitsToInt
        raiseToPower d = d ^ nOfDigits
        sumAllToPower = toInteger . sum $ map raiseToPower digitsToInt


