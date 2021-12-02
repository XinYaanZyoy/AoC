module Challanges.Day1 where

allEntriesStr :: FilePath -> IO [String] 
allEntriesStr path = do
    report <- readFile path
    return (lines report)

strToInt :: String -> Integer
strToInt str = read str :: Integer

allEntriesInt :: FilePath -> IO [Integer]
allEntriesInt path = do
    ins <- allEntriesStr path    
    let outs = map strToInt ins
    return outs

runA :: IO [(Integer, Integer, Integer)]
runA = do
    xs <- allEntriesInt "./data/ins/Day1.input"
    return [(a, b, a*b)| a <- xs, b <- xs, a+b==2020]

runB :: IO [(Integer, Integer, Integer, Integer)]
runB = do
    xs <- allEntriesInt "./data/ins/Day1.input"
    return [(a, b, c, a*b*c) | a <- xs, b <- xs, c <- xs, a+b+c==2020]
