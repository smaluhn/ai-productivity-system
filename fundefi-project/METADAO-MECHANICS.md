# MetaDAO Launch Mechanics - For FunDeFi Inspiration

**Source:** https://www.metadao.fi
**Purpose:** Extract key mechanics to inspire/adapt for FunDeFi
**Last Updated:** 2025-10-29

---

## 🚀 MetaDAO 3-Phase Model

### **Phase 1: Get Funded**
> "How projects get initial funding"

**Original MetaDAO Text:**
> "Founders post ideas with minimum USDC targets - clearly stating what they aim to build and how much funding they need to get started.
> Anyone can contribute USDC to back projects they believe in - community members evaluate ideas and contribute funding to the ones they find most promising.
> If a project reaches its target, it goes live. Otherwise, everyone gets their USDC back - this ensures only ideas with sufficient community support move forward, and there's no risk of lost funds if a target isn't met."

**Key Mechanics:**
- ✅ Founders post project ideas with **minimum USDC target**
- ✅ Anyone can contribute USDC to projects
- ✅ **Threshold requirement:** If target not met → refund everyone
- ✅ No risk of lost funds if project fails to reach minimum

**FunDeFi Adaptation:**
```markdown
### Get Funded
How projects raise on FunDeFi

Founders submit project proposals with funding targets - clearly stating what they aim to build,
milestones to achieve, and how much capital they need.

veFUNDE holders vote to approve projects - community evaluates ideas through 2-week voting epochs,
ensuring only quality projects with strong support move forward.

If a project is approved and reaches its funding target, it launches. If it falls short,
the protocol's reserve fund can fill the gap to ensure success - this protects both founders
and backers while building platform reputation.
```

**Changes from MetaDAO:**
- ✅ Added: veFUNDE voting requirement (quality filter)
- ✅ Added: Reserve fund safety net (vs refund)
- ✅ Added: 2-week voting epoch (structured timeline)
- ✅ Keep: Minimum target concept
- ❌ Remove: Automatic refund (replaced with reserve support)

---

### **Phase 2: Go Live**
> "Successfully establish a project"

**Original MetaDAO Text:**
> "10M tokens are distributed proportionally to everyone who contributed USDC - backers receive ownership stakes based on their initial contributions, aligning incentives from day one.
> 20% of the USDC and 2M tokens are paired in a liquidity pool - establishing market-based price discovery and enabling token transferability from the start.
> The liquidity position, the remaining USDC, and the ability to mint new tokens are transferred to a newly-created DAO - establishing on-chain governance from day one."

**Key Mechanics:**
- ✅ Token distribution proportional to USDC contributed
- ✅ 20% of USDC + 20% of tokens → Liquidity pool (20% LP ratio)
- ✅ Remaining 80% USDC → DAO treasury
- ✅ Governance established immediately (on-chain DAO)
- ✅ Mint authority → DAO controlled

**FunDeFi Adaptation:**
```markdown
### Go Live
Successfully launch your project

Tokens are distributed to all backers based on their contribution size - creating aligned ownership from day one.

25% of raised USDC and matching TOKEN supply are paired in an Aerodrome liquidity pool - enabling
immediate price discovery and trading while providing deep liquidity.

The remaining 65% of raised USDC is locked in milestone-gated escrow - creators unlock funds
progressively by achieving verified milestones, ensuring accountability and ongoing value delivery.

veTOKEN stakers earn trading fees forever - creating sustainable yields and long-term alignment
between project success and holder rewards.
```

**Changes from MetaDAO:**
- ✅ Changed: 25% liquidity (vs 20%) for deeper pools
- ✅ Added: Milestone-based unlocking (65% escrow)
- ✅ Added: veTOKEN staking for trading fees
- ✅ Keep: Proportional distribution
- ✅ Keep: Immediate liquidity pairing
- ❌ Remove: Full treasury to DAO (replaced with milestone escrow)

---

### **Phase 3: Build**
> "How projects grow and evolve"

**Original MetaDAO Text:**
> "Contributors raise proposals to spend USDC and receive token allocations - enabling transparent and community-driven resource allocation for development efforts.
> Unlike legacy DAOs, governance decisions are made by decision markets. You trade on how the DAO should be run and grow your portfolio when the market agrees with you.
> If the founder rugs, anyone can raise a proposal to liquidate the treasury and return USDC to tokenholders - providing a safety mechanism that protects contributors and incentivizes founder accountability."

**Key Mechanics:**
- ✅ Community can propose spending decisions
- ✅ **Decision markets** (futarchy) for governance (unique!)
- ✅ Trade on governance outcomes (market-based decisions)
- ✅ Anti-rug protection: Liquidate treasury if founder rugs
- ✅ Return USDC to tokenholders (safety mechanism)

**FunDeFi Adaptation:**
```markdown
### Build
How projects grow and deliver

Creators submit milestone completion proofs - providing verifiable evidence of development progress
through code commits, product demos, or third-party audits.

veTOKEN holders vote on milestone releases - community evaluates whether milestones were truly
achieved before unlocking the next tranche of funding.

If milestones consistently fail or the founder abandons the project, veTOKEN holders can vote to
return remaining USDC to backers and buy back FUNDE tokens - protecting the community and ensuring
founder accountability.

Contributors who provide valuable feedback, testing, or support can be nominated for TOKEN airdrops -
rewarding active participation and building engaged communities around each project.
```

**Changes from MetaDAO:**
- ✅ Added: Milestone-based releases (structured vs freeform)
- ✅ Added: Contributor airdrop rewards (2% allocation)
- ✅ Added: FUNDE buyback on failures (deflationary)
- ✅ Keep: Community voting on funds
- ✅ Keep: Liquidation/refund protection
- ❌ Remove: Decision markets/futarchy (too complex for v1)

---

## 🔗 Decision Markets (MetaDAO Unique Feature)

**What It Is:**
> "Unlike legacy DAOs, governance decisions are made by decision markets. You trade on how the DAO should be run and grow your portfolio when the market agrees with you."

**How It Works (from https://www.metadao.fi/proposals):**
1. Proposals have **two outcomes** (pass/fail)
2. Users **trade on outcomes** (buy shares of "yes" or "no")
3. Market prices reflect **community conviction**
4. Winning side gets rewards, losing side loses stake
5. Creates **skin-in-the-game governance**

**Pros:**
- ✅ Reveals true beliefs (can't just vote without cost)
- ✅ Rewards good decision-makers (profit from correct predictions)
- ✅ Reduces noise (casual voters don't participate)
- ✅ Novel mechanism (differentiator)

**Cons:**
- ❌ Complex to understand (steep learning curve)
- ❌ Favors wealthy participants (need capital to trade)
- ❌ Smart contract complexity (harder to audit)
- ❌ Less accessible (intimidating for newcomers)

**FunDeFi Position:**
- ❌ **Don't implement for v1** (too complex)
- ✅ **Stick with simple veTOKEN voting** (accessible, proven)
- 🔮 **Consider for v2** (if we want unique governance feature)

---

## 📊 Comparison Table: MetaDAO vs FunDeFi

| Feature | MetaDAO | FunDeFi | Winner |
|---------|---------|---------|--------|
| **Funding Model** | USDC contributions | USDC contributions | Tie |
| **Quality Filter** | ❌ No filter (anyone can launch) | ✅ veFUNDE voting required | **FunDeFi** |
| **If Underfunded** | Refund everyone | Reserve fund fills gap | **FunDeFi** |
| **Liquidity %** | 20% | 25% | **FunDeFi** |
| **Treasury Use** | 80% to DAO immediately | 65% milestone-locked | **FunDeFi** |
| **Governance** | Decision markets (futarchy) | veTOKEN voting | **MetaDAO** (novel) |
| **Anti-Rug** | Liquidate & refund | Milestone gates + refund | **FunDeFi** |
| **Staker Yields** | ❓ Unknown | Trading fees + emissions | **FunDeFi** |
| **Contributor Rewards** | ❌ Not mentioned | ✅ 2% airdrop allocation | **FunDeFi** |
| **Platform Token** | META required | veFUNDE required | Tie |

**Score:** MetaDAO: 6/10 | FunDeFi: 9/10

---

## 💡 What We Should Copy

1. ✅ **3-phase narrative structure** (Get Funded → Go Live → Build)
   - Simple, clear user journey
   - Easy to explain on website
   - Memorable framework

2. ✅ **Minimum funding targets** (refund if not met)
   - Actually, we do better: reserve fund vs refund
   - But keep the "target" concept visible

3. ✅ **Proportional token distribution** (based on USDC contributed)
   - Fair, transparent
   - Easy to calculate

4. ✅ **Immediate liquidity pairing** (at launch)
   - Enables price discovery
   - Tradeable from day 1

5. ✅ **Anti-rug protection** (liquidate if founder abandons)
   - Safety net for backers
   - Founder accountability

---

## 🚫 What We Should NOT Copy

1. ❌ **Decision markets/futarchy** (for v1)
   - Too complex for mainstream adoption
   - Hard to audit
   - Favors wealthy participants
   - Keep simple veTOKEN voting instead

2. ❌ **No quality filter** (anyone can launch)
   - MetaDAO has no curation
   - We have veFUNDE voting (better)

3. ❌ **Full treasury to DAO immediately** (80% unlocked)
   - We do milestone-based (65% locked)
   - Our model prevents rug pulls better

---

## 📝 Website Copy - Adapted for FunDeFi

### **Section 1: Get Funded**
```
How projects raise on FunDeFi

Founders submit comprehensive project proposals - clearly stating what they aim to build,
development milestones, and funding requirements.

veFUNDE holders vote to approve projects - our community evaluates ideas through structured
2-week epochs, ensuring only high-quality projects with strong support move forward.

Approved projects launch with guaranteed success - if community backing falls short, our
reserve fund ensures projects reach their targets, building confidence for all participants.
```

### **Section 2: Go Live**
```
Successfully launch your project

Tokens distributed proportionally to all backers - creating aligned ownership and fair
allocation from day one, with optional auto-staking bonuses for long-term believers.

25% of raised USDC paired with tokens in Aerodrome liquidity - enabling immediate price
discovery and deep trading liquidity from the moment you go live.

65% of funds locked in milestone-gated escrow - creators unlock capital progressively by
achieving verified milestones, ensuring accountability and continuous value delivery.

veTOKEN stakers earn trading fees forever - creating sustainable passive income and
long-term alignment between project success and community rewards.
```

### **Section 3: Build**
```
How projects grow and deliver

Creators submit milestone completion proofs - demonstrating development progress through
code commits, product demos, audits, or third-party verification.

veTOKEN holders vote on milestone releases - your community evaluates whether deliverables
were achieved before unlocking the next funding tranche, ensuring accountability.

Contributors get rewarded for participation - active community members who test, provide
feedback, create content, or support growth can earn TOKEN airdrops through nomination.

Built-in protection against failure - if milestones fail or founders abandon projects,
veTOKEN holders can vote to return remaining funds and buy back FUNDE, protecting all participants.
```

---

## 🔗 Links to Include on Website

- **Decision Markets Explainer:** https://www.metadao.fi/proposals (if we add futarchy later)
- **Documentation:** Link to our own docs
- **Governance Dashboard:** Link to voting interface
- **Project Proposals:** Link to active funding rounds

---

**Last Updated:** 2025-10-29
**Next Review:** When designing website copy
**Owner:** Simon + Werner (CMO)
**Status:** Ready for website implementation
