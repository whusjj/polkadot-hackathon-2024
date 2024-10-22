# Project XXX
Each project must provide the sufficient information, please check all mandatory parts as follows.

-- mandatory parts
## Introduction
-- project name

-- project creation date

-- project background, including github link before, won any rewards before, got any grant from web3 foundation and so on

MEV, or Maximal Extractable Value, refers to the maximum value that can be extracted from users in a blockchain network by reordering, inserting, or canceling transactions. This value typically comes from arbitrage opportunities, liquidation operations, and other types of transaction priority handling. The concept of MEV was initially widely discussed in the Ethereum network, but it also applies to other blockchain platforms that support smart contracts. Opportunistic traders extract monetary value from the network of decentralized finance (DeFi) smart contracts through what is known as MEV. Quantitative studies have shown that MEV can undermine the consensus security of blockchains; for example, if MEV opportunities exceed block rewards by four times, a rational miner with 10% of the hash rate would fork Ethereum.

The core principle of MEV is the manipulation of transaction ordering. Simply put, miners or validators have the freedom to choose which transactions to include in the blocks they construct and can arrange these transactions in any order. This power allows them to maximize their own profits by optimizing the transaction sequence. A typical example is the sandwich attack: miners or validators can observe transactions in the mempool (a pool of unconfirmed transactions) and act on this information to execute profitable operations in advance, such as front-running the same transactions to capture price differentials. Once the target transaction is completed, the attacker executes a sell transaction to sell the previously purchased assets at a higher price, thereby realizing a profit. Sandwich attacks not only deprive victims of their profits but can also maliciously manipulate asset prices.
Over a period of 32 months starting from 2018, MEV generated 5.4 M USD profit, among which sandwich attack generated 1.73 M USD profit.

There have been some proposals to solve this problems.Flashbots is an open-source project aimed at reducing the negative impacts of MEV. It does this by establishing an independent auction system to handle transactions, thus avoiding the front-running issues that occur in standard memory pools. Flashbots introduces the concept of "private transactions," allowing users and searchers to submit transactions directly to miners or validators with higher gas fees, bypassing the public memory pool. This effectively prevents MEV-related manipulative behaviors such as sandwich attacks.MEV-Boost is another solution that enables nodes to obtain blocks from block relays. It can either automatically build blocks or inspect block headers and retrieve blocks from professional block builders. Builders pay a certain fee to be prioritized for inclusion. This method redistributes a portion of the MEV but introduces additional trust assumptions regarding relay nodes.However, both of these methods still struggle to prevent significant asset value fluctuations that can be caused by MEV.

We have developed No Sandwich Swap, an MEV-resistant DEX that uses a hyperbolic batch auction mechanism. This mechanism aggregates multiple transactions over a certain period and then infinitely subdivides and uniformly interleaves them, thereby smoothing out the price impact of individual transactions and dispersing the trades of MEV attackers throughout the entire cycle, significantly reducing their arbitrage profits. Based on this approach, we have proven that the upper bound of asset price volatility within each phase is O(n^1/2), where n is the absolute value of the difference between the amounts of funds sold and bought over a certain period. Our protocol operates on an order placement and settlement model, collecting orders over a certain period before entering the settlement phase, which repeats cyclically.

## Features planned for the Hackathon
-- The status of project before participate the Hackathon

-- Features are planed for the Hackathon

## Architect
-- Diagram of architect for the project

-- Description for each components

## Schedule
-- timeline for all activities of your project during Hackathon

-- important milestone like first submit, pre-demo, testnet

-- completed features, tests, docs or in production

## Team info
-- all team members and each one's background

-- contact info for each one, email, github hander and so on

## Track and bounty
-- track you choose

-- bounty you will apply


** mandatory before offline demo, submit aterial for Demo
1. Demo Video [link to Youtube]
2. PPT [link to google doc]

-- optional parts
1. tokenomics design
2. marketing plan
3. vc, investment
4. community growth
