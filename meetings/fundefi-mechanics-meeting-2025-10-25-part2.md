# FunDeFi Mechanics Discussion 2/2 - 2025-10-25

**Date:** 2025-10-25 (Friday)
**Time:** 6:06 PM
**Attendees:** Simon, Thuy
**Duration:** ~14 minutes
**Fireflies Recording:** https://app.fireflies.ai/view/01K8DDB4ZN26FBAHEQSQK2C27M

---

## Overview

Second part of FunDeFi tokenomics discussion finalizing the voting mechanism, fee structure, token distribution, and staking features for the FunDeFi launchpad platform.

---

## Key Decisions Made

### Voting & Epoch System
- ✅ **Two-week voting epoch** (instead of weekly) for better project promotion time
- ✅ **Voting power** based on amount of veFUNDE locked + duration locked
- ✅ **Incentive model:** Projects/anyone can add incentives (tokens or stablecoins) to attract voters
- ✅ **Distribution:** Proportional to voting power contributed

### Fee & Allocation Structure (from $ Funding)
- ✅ **10% Launchpad fee** (in USDT/stables):
  - **7.5%** → FunDeFi Protocol Vault
  - **2.5%** → TOKEN Vault (for buyback & veTOKEN staker yield)
- ✅ **25% for liquidity** (fixed, auto-graduate to partner DEX)
- ✅ **Remaining ~65%** goes to project treasury
  - **⚠️ LOCKED with milestone-based release**
  - Released via veTOKEN holder voting (governance)

### TOKEN Tokenomics (from $TOKEN supply)
- ✅ **2.5% → Launchpad allocation**
  - Auto-staked as veFUNDE for long-term Protocol Treasury
- ✅ **2.5% → Auto-Stakers**
  - Distributed to backers who choose auto-stake
- ✅ **2.5% → Airdrops**
  - Contributors (community-nominated feedback providers)
  - Marketers (top 3 on referral leaderboard)
  - Backers (all veFUNDE voters for the TOKEN)
- ✅ **92.5% → Project allocation** (liquidity, team, community, etc.)

### Token Distribution & Emissions
- ✅ **NO PROTOCOL EMISSIONS** - FunDeFi is a launchpad, NOT a DEX
  - No inflationary $FUNDE emissions
  - Cleaner tokenomics than traditional DeFi
- ✅ **Airdrops as vested VE tokens** (e.g., veLX locked for 3 months) to prevent dumping
- ✅ **Auto-staking option** at token purchase with 2.5% bonus allocation

### Staking Features
- ✅ **2% buy/sell tax** on new tokens → funds BOTH vaults:
  - **Project's TOKEN vault** (e.g., veLX vault for Project LX)
  - **FunDeFi Protocol vault** (protocol revenue share)
- ✅ **Automated staking pools** created for each launchpad project
- ✅ **Restaking feature** - auto-renew VE token locks at expiry
- ✅ **2.5% TOKEN allocation** for auto-stakers (immediate bonus)

### Incentive System
- ✅ **TOKEN Creator can offer incentives:**
  - TOKEN airdrops (of their new token)
  - Stablecoins (USDT, USDC, etc.)
- ✅ **Anyone can add incentives** to any TOKEN during 2-week epoch
- ✅ **5% fee on all incentives** → distributed to:
  - FunDeFi Protocol Vault
  - Contributors to platform development
- ✅ **Incentives distributed proportionally** to veFUNDE voters

### Project Setup Requirements
- ✅ **Creator must lock 100 veFUNDE** - Skin in the game requirement
- ✅ **Soft cap/minimum funding** - Minimum $ needed for project to proceed
- ✅ **Fund usage plan** - How funds will be used
- ✅ **1-4 Milestones** with:
  - Defined scope
  - Verifiable completion criteria
  - $ amount to be released per milestone
- ✅ **Milestone releases** require veTOKEN holder vote approval

### Minimum Voting Requirements (Anti-Spam)
- ✅ **At least 20 unique wallets** must vote for TOKEN
- ✅ **At least 1,000 veFUNDE total** voting power required
- ✅ Only after thresholds met can project start accepting bribes/incentives

### Service Pricing
- ✅ **~$2,500 fee** for creating/automating staking pools for projects

---

## Detailed Mechanism Breakdown

### 1. veFUNDE Voting Mechanism

**How it works:**
1. Users lock FUNDE tokens to get veFUNDE
2. Two-week voting epochs for projects
3. Projects offer incentives (e.g., 50 USDT or token airdrops) to attract voters
4. Anyone can add incentives to any project pool
5. Rewards distributed proportionally based on:
   - Amount of veFUNDE locked
   - Duration of lock (multiplier effect)

**Example:**
- User locks 100 veFUNDE and votes for Project X
- User receives proportional share of incentive pool
- If user has 0.7% of total votes → gets 0.7% of 50 USDT incentives

### 2. Fundraising & Fee Structure

**For a project raising 10K USDT:**

**$ Funding Distribution (USDT/Stables):**
- **10% (1K USDT)** → Launchpad fee:
  - **7.5% (750 USDT)** → FunDeFi Protocol Vault
  - **2.5% (250 USDT)** → TOKEN Vault (for buyback & veTOKEN yield)
- **25% (2.5K USDT)** → Liquidity pool (auto-graduate to partner DEX)
- **65% (6.5K USDT)** → Project treasury (**MILESTONE-LOCKED**)

**$TOKEN Distribution (from token supply):**
- **2.5%** → Launchpad allocation (auto-staked as veFUNDE for Protocol)
- **2.5%** → Auto-stakers (distributed to backers who auto-stake)
- **2.5%** → Airdrops (contributors, marketers, backers)
- **92.5%** → Project allocation (liquidity, team, community, etc.)

**Why fixed parameters?**
- Simplicity for projects (no decision paralysis)
- Prevents insufficient liquidity (common failure point)
- Can adjust model later after validation

**Project Treasury (65%) - Milestone-Based Release:**
- NOT released all at once
- Locked in smart contract
- Released in stages based on milestone completion
- Each release requires **veTOKEN holder vote approval**
- Protects backers from rug pulls and mismanagement

### 3. Token Airdrop Mechanism (2.5% of TOKEN supply)

**Three Categories of Recipients:**

**1. Contributors (Community-Nominated)**
- Users who provide valuable feedback on TOKEN in comments
- **Nominated by:**
  - TOKEN Creator (project team)
  - Community (veFUNDE voters for that TOKEN)
- **Award process:**
  - Community votes on which feedback was most helpful
  - Creator can also directly reward contributors
- **Purpose:** Incentivize quality feedback and due diligence

**2. Marketers (Referral Leaderboard)**
- Users who promote TOKEN using referral links
- **Tracked via leaderboard** during 2-week epoch
- **Top 3 rewards:**
  - 🥇 **1st place:** [X]% of marketing airdrop allocation
  - 🥈 **2nd place:** [Y]% of marketing airdrop allocation
  - 🥉 **3rd place:** [Z]% of marketing airdrop allocation
- **Metrics tracked:** Referrals, conversions, engagement
- **Purpose:** Incentivize organic marketing and growth

**3. Backers (veFUNDE Voters)**
- ALL users who voted for the TOKEN with veFUNDE
- **Distribution:** Proportional to voting power contributed
- **Purpose:** Reward early supporters and governance participants

**Distribution Method:**
- NOT liquid tokens (prevents dumping)
- Distributed as **veTOKEN** (e.g., veLX)
- **Locked for 3 months** minimum
- Creates aligned long-term incentives

**Benefits for veTOKEN holders:**
- Receive proportional share of 2% buy/sell tax
- Participate in milestone governance votes
- Tax flows to TOKEN vault → redistributed to veTOKEN stakers
- Creates sustainable reward mechanism

### 4. Auto-Staking Feature (2.5% TOKEN Allocation Bonus)

**At Token Purchase/Backing:**
- Buyer has option to "auto-stake" tokens
- **2.5% of TOKEN supply** distributed ONLY to auto-stakers
- Auto-stakers receive:
  - **Proportional share of 2.5% TOKEN pool** (immediate bonus)
  - **Ongoing share of 2% buy/sell tax** from TOKEN vault
  - **Boost rewards** (20-25% extra APY) for 1-3 months
  - **Governance rights** via veTOKEN

**Example:**
- User backs TOKEN with $100 USDT
- Chooses "auto-stake" option
- Receives:
  1. Base TOKEN allocation (from their $100)
  2. **Bonus from 2.5% auto-staker pool** (shared with all auto-stakers)
  3. **Ongoing yield from TOKEN vault** (2% tax revenue)
  4. **Voting power** for milestone releases

**Benefits:**
- Incentivizes long-term holding
- Reduces sell pressure at TGE
- Creates aligned token holder base
- Participants = governance voters for milestones

### 5. DUAL VAULT SYSTEM - Complete Revenue Model

#### **🏦 FunDeFi Protocol Vault**

**Inflows:**
1. **7.5% of launchpad fees** (in USDT from each fundraise)
2. **Portion of 2% buy/sell tax** from ALL launched TOKENs
3. **LP yield** from Protocol-owned liquidity positions
4. **5% of all incentive fees** (when users add bribes/incentives)
5. **$FUNDE usage fees** when used for protocol features/credits
6. **Portion of TOKEN usage fees** (when TOKENs used in ecosystem apps)

**Outflows (Redistributed to):**
- veFUNDE stakers (proportional to lock duration/amount)
- Protocol treasury for operations
- Development fund
- Marketing & ecosystem growth

**Purpose:**
- Sustainable protocol revenue without emissions
- Rewards $FUNDE holders for long-term alignment
- Funds ongoing platform development

---

#### **🏦 TOKEN Vault (per launched project)**

**Inflows:**
1. **2.5% of launchpad fees** (in USDT from that TOKEN's fundraise)
2. **Portion of 2% buy/sell tax** from TOKEN trading
3. **LP yield** from TOKEN's DEX liquidity pool
4. **TOKEN usage fees** when used for apps/credits in ecosystem
5. **Buyback mechanism** using USDT from vault

**Outflows (Redistributed to):**
- veTOKEN stakers (project-specific VE token holders)
- TOKEN buyback & burn (price support)
- Project development incentives
- Community rewards

**Purpose:**
- Sustainable project-level yield
- Price support through buybacks
- Rewards early backers and long-term holders

---

#### **Revenue Split Details:**

**2% Buy/Sell Tax Distribution:**
- **50%** → TOKEN Vault (benefits veTOKEN stakers)
- **25%** → FunDeFi Protocol Vault (benefits veFUNDE stakers)
- **25%** → Liquidity pool (deepens liquidity)

**Usage Fees (when TOKEN used for credits/features):**
- **60%** → TOKEN Vault
- **30%** → FunDeFi Protocol Vault
- **10%** → App/feature developer

**This creates:**
- **Triple circular economy** (project, platform, ecosystem)
- Incentive to hold both veFUNDE and veTOKEN
- Sustainable yield without protocol emissions
- Revenue alignment at all levels
- Buyback mechanism for price support

### 6. Restaking Feature

**Purpose:** Reduce friction for long-term holders

**How it works:**
- When VE token lock approaches expiry
- User can opt-in to auto-restake
- Automatically renews lock for chosen duration
- Maintains voting power and rewards

### 7. Milestone-Based Treasury Release System

**Purpose:** Protect backers and ensure accountability

**Project Setup Requirements:**
When creating a project, founders must define:

1. **Soft Cap/Minimum Funding**
   - Minimum $ needed for project to proceed
   - If not reached, funds returned to backers

2. **Fund Usage Plan**
   - Detailed breakdown of how funds will be used
   - Transparent allocation (dev, marketing, ops, etc.)

3. **Milestones (1-4 required)**
   - **Scope:** What will be delivered
   - **Verifiable Criteria:** How completion is verified
   - **$ Amount:** How much released upon completion
   - **Timeline:** Expected completion date

**Release Mechanism:**
1. Project completes milestone
2. Submits proof/evidence to community
3. **veTOKEN holders vote** on whether criteria met
4. If approved (e.g., >50% yes votes) → funds released
5. If rejected → project must remediate or provide more evidence

**Example Milestone Structure (10K raise, 6K treasury):**
- **Milestone 1 (2K):** MVP launch + 100 users - 30 days
- **Milestone 2 (1.5K):** 1,000 users + core features - 60 days
- **Milestone 3 (1.5K):** 5,000 users + partnerships - 90 days
- **Milestone 4 (1K):** 10,000 users + revenue generation - 120 days

**Benefits:**
- Protects backers from rug pulls
- Ensures project delivers on promises
- Creates accountability through governance
- veTOKEN holders have skin in the game (already investors)
- Gradual release reduces mismanagement risk

### 8. Automated Staking Pools

**Service for projects:**
- FunDeFi creates automated staking pool
- Built into launchpad
- Price: ~$2,500 per project

**Benefits:**
- Seamless UX for token buyers
- Encourages long-term holding
- Reduces sell pressure

---

## Action Items

### Unknown/Simon/Dev Team

**Core Voting & Staking:**
- [ ] Finalize two-week epoch voting mechanism with incentive structures
- [ ] Develop auto-staking functionality integrated into token purchase process
- [ ] Set up restaking feature allowing users to renew veToken staking automatically at lock expiry
- [ ] Implement 100 veFUNDE lock requirement for TOKEN creators
- [ ] Build minimum voting threshold checks (20 wallets, 1000 veFUNDE)

**Airdrop System:**
- [ ] Build contributor nomination and voting system
- [ ] Create referral link tracking and leaderboard system
- [ ] Define exact reward splits for top 3 marketers (1st, 2nd, 3rd place %)
- [ ] Implement veTOKEN distribution mechanism (3-month vesting)

**Vault Mechanics:**
- [ ] Design dual vault system (Protocol + TOKEN vaults)
- [ ] Implement 2% buy/sell tax split (50% TOKEN, 25% Protocol, 25% LP)
- [ ] Build buyback mechanism for TOKEN vaults
- [ ] Create usage fee tracking and distribution system
- [ ] Implement 5% incentive fee collection and distribution

**Milestone Governance:**
- [ ] Design milestone-based treasury release smart contract
- [ ] Build veTOKEN holder voting interface for milestone approvals
- [ ] Create project setup form with soft cap, milestones, and verifiable criteria fields
- [ ] Implement milestone verification and evidence submission system
- [ ] Design governance threshold for milestone releases (>50% approval)

**Tokenomics:**
- [ ] Finalize TOKEN distribution (2.5% launchpad, 2.5% auto-stakers, 2.5% airdrops)
- [ ] Implement 2.5% launchpad allocation auto-staking as veFUNDE
- [ ] Calculate and optimize revenue splits across all mechanisms

**Service & Pricing:**
- [ ] Establish pricing structure (~$2,500) for automated staking pool service
- [ ] Create visual diagram of complete FunDeFi mechanism (CRITICAL)

### Design/Documentation
- [ ] Simplify presentation of complex tokenomics
- [ ] Create user-friendly explanation materials
- [ ] Design flow charts for voting, staking, and reward mechanisms

---

## Full Transcript

**Simon:** The second one. Okay, so now to continue the ve Fundi voting. Yeah. So what should the mechanism be like? So let's say we have a weekly epoch, right? So. So then we have like different projects on our platform. So then the projects we want the users to be active to vote, right? So they will be voting for the projects for the new tokens. And then like.

Okay, we have like let's say 10 projects. They all receive like this one receive 7%, 10%, 15%, 2% of the tokens in total from all the ve. Ve. Fundy. Sorry. Ve Fundi voters. Right. That they lock it for this week's epoch to the. To these different tokens to these different projects. Then what's the mechanism? How does it work? So what's the benefit that they get these votes?

So for example, one way, one thing we could do is that we say that a project has to receive a minimum of unique voters or a minimum of and. Or minimum of received votes this week. So. So they are able to actually do the fundraise. And also we could do the. Do you know what I mean?

**Thuy:** Oh, a little bit. Like you want to do it or you consider.

**Simon:** Right, consider. So I'm wondering like how about the bribe system, the incentive system and the voting system like you know.

**Thuy:** Yeah. I project if they want to promote user to vote for them to launch on the platform, right. They need to provide something like air drop tokens are stable up to.

**Simon:** Okay.

**Thuy:** Yes. So like and then maybe they can have two weeks for voting rights and in the two week they just promote. Like if you vote for us we. You can have like the 50k50 in tokens are unstable right after the project and then after finish it on the users vote for them, they can receive it just simple.

**Simon:** So like a simple airdrop voting campaign.

**Thuy:** So very simple. So the project they can give the incentive and then anyone also can give incentive and these incentives will go to the voters. And these incentives can either be the token, the newly generated token as an airdrop and. Or stable.

**Simon:** Yes, yes. Just make it simple.

**Thuy:** Okay.

**Simon:** Okay. Understand?

**Thuy:** Yes.

**Simon:** Okay. Yes. Okay, makes sense. And then maybe it's like this. If I'm the. So I use the V Fundy. Ve fundi. So then I vote for your project. So then I can receive, you know, depending on how many votes I give, maybe I give 100 ve fundi. And then you know, there are so many others. And then I get like relative, you know, maybe I have like 0.7% so I get 0.7% of this 50 USDT.

**Thuy:** Stable and to the VE voting power. Yeah, that they have answer how many users use distribute to the pool, you know, like how many user vote in that pool and then up to the voting power, you know?

**Simon:** Right. This is also on the voting power. So the longer I have staked the fundy token for the to get the VE fundi, the more voting power or the multiplier. I have.

**Thuy:** More tokens for. For to receive the ve.

**Simon:** Right. It like. Of course, like for people who lock 100 tokens will have more benefit than user only lock 1 tokens.

**Thuy:** Yes. So you need to make it, you know that mechanism.

**Simon:** Yes, yes, yes. Okay. And then so. And then the other mechanism is that anyone can maybe like I really. I'm Maybe I really like your project. So I also give an incentive. So I add another incentive. Oh, I also give 30 USDT stable 2 as an incentive for all the voters for your project.

**Thuy:** Of course, like for adding liquidity. You make the mechanism that anyone can add it.

**Simon:** Ah, this one also. This is a separate new function I show you.

**Thuy:** Yes. Price, right?

**Simon:** Yes. Anyone can add the incentive and the. Incentive or the liquidity. You mean now?

**Thuy:** No, incentive.

**Simon:** Incentive. Okay. Not delete that about liquidity. Just incentive.

**Thuy:** Yes. Everybody can add in whenever pool that you want.

**Simon:** So yeah. So you have your new token and. Then they want to win, they can add more.

**Thuy:** Yes, yes.

**Simon:** So you have your token and then in this week's epoch or two week, you said like two weeks. You think it should be two weeks instead of one week.

**Thuy:** The time frame normally we need to be in two weeks.

**Simon:** Two weeks. So better two weeks than one week. Okay, so let's fix two weeks instead of one week epoch. So then the.

**Thuy:** We drink much water.

**Simon:** Okay, so then. And then the protocol doesn't give any emissions. Right. So we don't give any fundy token. We are lunch pack. We're not dex.

**Thuy:** Yes, right. We are lunch pads.

**Simon:** We are launchpad. We are not de. So we don't give any emissions. We have them raise money.

**Thuy:** Yes, it's a good thing already.

**Simon:** So we don't give anything. We. Which is great. So it's one less deflationary mechanism. Great.

And then what about the mechanism? So I'm the fundy voter for your project. Right. So then I can get the incentives from the incentive pool. Right. According to, you know, how many people vote, etc. How much is inside and so on.

And then also how should the minimum allocation or the minimum or the maximum, I mean the allocation be decided? So for example, for you're the Token, Right. You say. And how should the process be? So you're the token. So you say, oh, I want to raise 10k. Right. For example. Right? Yeah. Then.

Then there's one question about how much should go for. Let's say there's like 5%, 7%. 10% going to protocol. Right. For fees.

**Thuy:** 10.

**Simon:** 10. So 10 is going launchpad fee. Okay, next then how much to liquidity?

**Thuy:** No, the token needs liquidity. But you don't need. You are not Dex. Right?

**Simon:** No, no. We. We will work with another decks and then we. We auto graduate to the decks. So normally like normal lunch b have the same model with you. They will have to ask 25% all the Serine lunch pad. The what?

**Thuy:** For the Seren AI LP.

**Simon:** Yes. So they will let the father. They. The father decide. So on the money, we will look in the wallet and then the founder will decide how many percent can go to the liquidity pool.

**Thuy:** So we should give this flexibility, you think? Or should we fix it at 25 or whatever percentage?

**Simon:** Let's see. But some. Because they need to raise money, right? Of course, the 25%. Like you, like you think, like if they raise 10K, 25% of 10K is like.

**Thuy:** Yes, 2.5K exactly.

**Simon:** And then also if 10% goes to Launchpad and let's say 5% goes to AirDrop. No, it means 60% left.

**Thuy:** No.

**Simon:** Yeah, 60% left, which is actually not so bad. I mean, on pink sale, when people used to do that, that you. I mean, because it's the thing. If you only give. If you raise only 10k and you can do like 1 10%, like 1k liquidity, you know, there's no liquidity. It doesn't make any sense.

**Thuy:** For the flip flop, they give 20%, 25% for liquidity.

**Simon:** Yeah, like minimum or fixed.

**Thuy:** I think fixed.

**Simon:** So we could also do. Because I think if we give flexibility, then people need to think this and that. So I rather come up with a great model, you know, and then we can change the model and then later maybe we can give flexibility. I'm not sure. I mean, virtual IO. I think they. You can customize everything, but it's like too complicated. I want to make it very simple.

**Thuy:** So, so, okay, so we fix 10% Launchpad fee, 25% goes to liquidity. And. And then what else? So we have like. What about the token airdrop here?

**Simon:** My idea for the token airdrop is that the airdrop actually is not. Is in illiquid tokens. Not illiquid tokens. So it Will the new token. So okay, let's go back. So this is the mechanism, right? And the distribution.

So then let's say, let's say I don't know, maybe 5% is reserved for token airdrop and the token airdrop is distributed to the voters and also to everyone that gives feedback, the contributors and to the marketers that do a social media marketing with their referral link. Right.

Then, then the other, then the mechanism is that you don't get the token airdrop@tge to just cash out and dump it and so on. I don't think that is good and that works. But you will receive the VE token. So for example, you have like, you know, Alex token, right? So you will get VE lx already locked or staked, I mean for maybe three months only, right?

And then so, and I am the Arab recipient. So I receive this because we don't want to just give like free money to people, you know, for doing that. But now you will ask, oh, but then you know, blah blah blah. It's like state what's the benefit? The benefit is like this. Now keep, keep this in mind. But I need to first share the complete picture.

You have the VE token airdrop, okay. For everyone that, that contributes, that votes and that markets the thing and then also the backers, right? The so I give the money, right? So I put a hundred dollars. Then I have the option to auto stake. If I auto stake, I will get some benefit. Not I, I will maybe get also more tokens directly. So there's like an incentive to stake it.

So maybe there's actually, Maybe there's actually 2.5% to for airdrops and 2.5% for staking incentive. And this one will directly go proportionate to the auto stakers. So so maybe there's 2.5% or 5%. We need to run some calculations to test it.

So for example, let's say that 2.5% goes to the ad marketing airdrops and then 2.5% goes to the auto stakers. So if I buy the token for $100 and I choose auto stake, the 2.5% staking pool at the launch will directly go to everyone that chooses auto stake when buying.

And then what's the benefit? The benefit is the V, the token, the new token, the Alex token. When this is bought and sold we have buy and sell tax 2%. This is team being distributed to the protocol, to the vault and the vault is directly going then to the VE token. Like VE Alex token.

For example stakers and anyone that auto stakes also they will get let's say not only like extra tokens from the staking pool from the vault that is being you know, from the tokenomics of the token of the newly created token. Maybe this only and or additionally the some boost extra maybe like 20% or something or 25% extra for like you know, like three months or like one month or something like this.

Does it make sense? I mean do do offers. Does it? Is it understandable?

**Thuy:** And then I can understand a little bit.

**Simon:** Yes, I know it's a little bit complex, but I, I, I really try to make like a complete mechanism. And afterwards I will work on this to present it Also draw a mask.

**Thuy:** Yes, yes, yes, yes. Please draw a map about this.

**Simon:** Oh, already? Yes, okay. I think it's okay. But try to make everything not too complex.

**Thuy:** Yes, yes, yes, yes, yes, yes.

**Simon:** And then also one, one feature separate from this is we can have the restaking feature. Right? So for example, if it already almost expires the ve staking of like the protocol token or the newly created tokens, then the user has the staker has the option to auto to restake. Right?

**Thuy:** Yeah. Yeah.

**Simon:** Can you help project create a stacking pool?

**Thuy:** Yes, they will automate. Oh, this is the, this is the nice thing about our launchpad. There's already a staking pool directly created on our launchpad.

**Simon:** I mean like I before that I set stacking PO service.

**Thuy:** Oh yeah, Yeah. I think we can spot work. We just take around 2,500. How about you?

**Simon:** Yeah, I think we can do it. Project need to create a stacking pool.

---

## Visual Summary Needed

**Simon's request:** Create a visual map/diagram of the complete mechanism

**What needs to be visualized:**
1. User flow: $FUNDE → veFUNDE → Voting
2. Project flow: Fundraising → Distribution (10% fee, 25% liquidity, 5% airdrops/staking, 60% milestone-locked treasury)
3. Incentive flow: Project/supporters add incentives → distributed to voters
4. Staking flow: Auto-stake option → bonus rewards → vault rewards
5. Tax flow: 2% buy/sell → dual vaults (project + FunDeFi) → VE stakers
6. Restaking loop: Auto-renewal of VE locks
7. **Milestone governance flow: Milestone completion → veTOKEN vote → Treasury release**

---

## Keywords

- $FUNDE token
- veFUNDE voting (100 lock for creators)
- veTOKEN governance
- two-week epoch
- minimum thresholds (20 wallets, 1000 veFUNDE)
- launchpad mechanism
- three-tier airdrop (contributors, marketers, backers)
- 2.5% auto-staker bonus
- staking incentives
- liquidity allocation
- restaking feature
- auto-staking
- 2% buy/sell tax (50% TOKEN, 25% Protocol, 25% LP)
- dual vault system (Protocol + TOKEN)
- no emissions model (ZERO inflation)
- milestone-based treasury (65% locked)
- soft cap funding
- community governance
- rug pull protection
- buyback mechanism
- 5% incentive fees
- referral leaderboard
- usage fees (30% Protocol, 60% TOKEN)
- 2.5% launchpad TOKEN allocation

---

## 📊 COMPLETE FUNDEFI MECHANICS SUMMARY

### 🎯 Platform Overview
**FunDeFi** is a community-governed launchpad with NO emissions, milestone-based treasury releases, and a dual vault system that creates sustainable yields for both platform and project stakeholders.

---

### 💎 Key Differentiators

| Feature | Traditional Launchpad | FunDeFi |
|---------|----------------------|---------|
| **Community voting** | No | ✅ veFUNDE 2-week epochs |
| **Creator commitment** | None | ✅ 100 veFUNDE lock required |
| **Launch threshold** | None | ✅ 20 wallets + 1000 veFUNDE minimum |
| **Emissions** | Often yes (inflationary) | ✅ ZERO (deflationary) |
| **Treasury release** | Immediate (rug risk) | ✅ Milestone-locked + governance |
| **Staking** | Manual | ✅ Auto-stake with 2.5% bonus |
| **Airdrops** | Liquid (dumping) | ✅ Vested veTOKEN (3mo lock) |
| **Airdrop system** | Generic | ✅ Contributors + Marketers + Backers |
| **Revenue model** | Single tier | ✅ Dual vault (Protocol + TOKEN) |
| **Accountability** | None | ✅ veTOKEN governance votes |
| **Incentives** | Platform only | ✅ Anyone can add + 5% fee |
| **Buyback** | Rare | ✅ Built-in from TOKEN vault |

---

### 💰 Complete Fee & Distribution Structure

#### **From $10K USDT Fundraise:**

**USDT Distribution:**
- 7.5% (750) → FunDeFi Protocol Vault
- 2.5% (250) → TOKEN Vault (buyback & yield)
- 25% (2,500) → DEX Liquidity Pool
- 65% (6,500) → Project Treasury (MILESTONE-LOCKED)

**$TOKEN Distribution (from supply):**
- 2.5% → Launchpad (auto-staked as veFUNDE)
- 2.5% → Auto-stakers bonus pool
- 2.5% → Airdrops:
  - Contributors (nominated by community/creator)
  - Marketers (top 3 leaderboard)
  - Backers (veFUNDE voters)
- 92.5% → Project (liquidity, team, community)

---

### 🏦 Dual Vault Economics

#### **FunDeFi Protocol Vault Receives:**
- 7.5% of all launchpad fees (USDT)
- 25% of 2% buy/sell tax from ALL TOKENs
- 5% of all incentive fees
- 30% of usage fees (TOKEN/FUNDE used in apps)
- LP yield from protocol-owned liquidity

#### **TOKEN Vault (per project) Receives:**
- 2.5% of launchpad fees (USDT from own raise)
- 50% of 2% buy/sell tax (from own trading)
- 60% of usage fees (when TOKEN used in apps)
- LP yield from TOKEN's liquidity pool

**Redistribution:**
- Protocol Vault → veFUNDE stakers
- TOKEN Vault → veTOKEN stakers + buybacks

---

### 🗳️ Anti-Spam & Quality Control

**Creator Requirements:**
- Lock 100 veFUNDE (skin in the game)
- Define soft cap + milestones
- Provide verifiable completion criteria

**Launch Requirements:**
- ≥20 unique wallet votes
- ≥1,000 total veFUNDE voting power
- Only then can accept bribes/incentives

**Governance:**
- veTOKEN holders vote on milestone releases
- Protects backers from rug pulls
- Ensures project accountability

---

### 🎁 Three-Tier Airdrop System (2.5% of TOKEN)

1. **Contributors:**
   - Provide valuable feedback in comments
   - Nominated by creator OR community vote
   - Rewards due diligence and quality analysis

2. **Marketers:**
   - Use referral links to promote TOKEN
   - Leaderboard tracked during 2-week epoch
   - Top 3 receive tiered rewards

3. **Backers:**
   - ALL veFUNDE voters for the TOKEN
   - Proportional to voting power
   - Rewards early supporters

**All distributed as 3-month locked veTOKEN**

---

### 🔄 Revenue Streams (NO EMISSIONS!)

**FunDeFi Protocol Vault:**
- Launchpad fees (7.5% of all raises)
- Trading taxes (25% of 2% tax from all TOKENs)
- Incentive fees (5% of all bribes)
- Usage fees (30% when FUNDE/TOKENs used)
- LP yield

**TOKEN Vaults (each project):**
- Launchpad fee portion (2.5% of own raise)
- Trading taxes (50% of 2% tax from own trading)
- Usage fees (60% when own TOKEN used)
- LP yield
- **Used for buybacks + veTOKEN rewards**

---

### ⚡ Auto-Staking Bonus

**Backers who choose auto-stake receive:**
- 2.5% of TOKEN supply bonus (shared proportionally)
- Ongoing yield from TOKEN vault
- 20-25% APY boost for 1-3 months
- Voting rights for milestones

**Creates:**
- Aligned long-term holders
- Reduced sell pressure at TGE
- Governance participants = investors

---

### 🛡️ Investor Protection

**Milestone-Based Treasury:**
- 65% of raise locked in contract
- 1-4 milestones with verifiable criteria
- veTOKEN holders vote to release funds
- Gradual release reduces risk
- Accountability built-in

**Example (10K raise):**
1. Milestone 1 (2K): MVP + 100 users @ 30 days
2. Milestone 2 (1.5K): 1K users + features @ 60 days
3. Milestone 3 (1.5K): 5K users + partnerships @ 90 days
4. Milestone 4 (1K): 10K users + revenue @ 120 days

---

### 🚀 Incentive Mechanism

**Anyone can add incentives to any TOKEN:**
- TOKEN creator offers bribes (TOKENs or stables)
- Community members can add more
- 5% fee on all incentives → Protocol vault
- Distributed proportionally to veFUNDE voters
- Creates competitive market for best projects

---

### 📈 What Makes This Sustainable?

1. **NO EMISSIONS** = No inflation
2. **Dual vaults** = Multiple revenue streams
3. **Usage fees** = Ecosystem value capture
4. **Buyback mechanism** = Price support
5. **Milestone governance** = Quality projects
6. **Auto-staking incentive** = Long-term holders
7. **3-month veTOKEN vesting** = Aligned interests
8. **100 veFUNDE creator lock** = Serious projects only

---

## Next Steps

1. Create visual diagram of complete FunDeFi mechanism (CRITICAL)
2. Test percentage allocations with sample scenarios
3. Build out technical specifications for:
   - Voting mechanism
   - Auto-staking feature
   - Restaking functionality
   - Automated staking pool creation
4. Simplify explanation for users/projects
5. Develop service pricing structure

---

## Philosophy & Design Principles

**Simplicity over flexibility:**
- Fixed parameters (10% fee, 25% liquidity) prevent decision paralysis
- Can evolve later after market validation

**Aligned incentives:**
- VE token airdrops (not liquid) prevent dumping
- Auto-staking creates long-term holders
- Buy/sell tax creates sustainable rewards

**No emissions = deflationary:**
- Launchpad model (not DEX)
- Projects raise money without protocol dilution
- Cleaner tokenomics

**User experience focus:**
- Automated staking pools
- Restaking feature reduces friction
- Clear reward mechanisms

---

**For full project details, see:** [projects/fundefi.md](../projects/fundefi.md) _(if exists)_

**Created:** 2025-10-25
**Last Updated:** 2025-10-25
