# RPS Markov Chain AI

A Rock Paper Scissors AI that learns and predicts human patterns using Markov Chains.

## How it works
- **1st Order Markov Chain**: predicts your next move based on your last move
- **2nd Order Markov Chain**: predicts based on your last two moves
- Both chains are combined with a 60/40 weighting for optimal prediction
- Laplace Smoothing prevents zero division and ensures all moves stay valid options

## Results
- ~44% win rate against random play
- ~92% win rate against fixed patterns

## Run
python RPS_PR.py
