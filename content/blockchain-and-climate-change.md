Title: Blockchain and Climate Change
Date: 2018-11-18 11:00
Author: markmc
Tags: Climate Change
Slug: blockchain-and-climate-change
Status: draft

*Disclaimer: Relative to my expertise in something like OpenStack, or
relative to the expertise of folks who are working daily on driving
advancements in the fundamentals of Blockchain and related
technologies, I know next to nothing about Blockchain. However,
relative to the average member of the public, I believe I have enough
understanding as a technologist to help demystify the subject for
other non-experts*.

The context for this post is that I attended the recent [Climate
Innovation Summit](https://www.climateinnovationsummit.org/) in
Dublin, which primarily focused on the challenge of financing
solutions in the area of Climate Change mitigation and adaptation. To
my surprise, the subject of Blockchain seemed to be the main pure
technology topic that came up again and again.

Before this event, and without exploring the area too deeply, I had a
suspicion that Blockchain is all too often "a solution in search of a
problem". This all too common tendency of technologists makes me
grumble at the best of times, but when the subject is a technology
that is impenetrable to many people, and the problem space is what I
believe to be an existential threat to our way of life ... I have
grave reservations, to put it mildly.

Much credit goes to EIT Climate-KIC for publishing a report titled
[Distributed Ledger Technology for Climate Action
Assessment](https://www.climate-kic.org/wp-content/uploads/2018/11/DLT-for-Climate-Action-Assessment-Nov-2018.pdf)
which I will refer to heavily below. In large part, my goal here is to
highlight the key points and conclusions I took away from that
report.

## What Problem Does Blockchain Solve?

Blockchain is designed to be an alternative to centralized
systems. What does that mean? Well imagine:

- A database with no central administrator
- A currency with no central bank
- A contract that is enforceable without recourse to a judiciary

and you start to get a sense of this problem space. This is quite
appealing, on the face of it. A decentralized system should be more
fault tolerant and attack resistant because there is no single point
of failure, and it should also be more trustworthy and resistant to
abuses of power because of the transparency it offers.

And then there's the idea of "social scalability", as [researcher Nick
Szabo is
quoted](http://unenumerated.blogspot.com/2017/02/money-blockchains-and-social-scalability.html)
in the Climate-KIC report:

> Scaling human traditional institutions in a reliable and secure
> manner requires increasing [the number of] accountants, lawyers,
> regulators, and police, along with the increase in bureaucracy,
> risk, and stress that such institutions entail."

Solving problems without needing needing any more lawyers? Hurrah!

## Why is Decentralization a Hard Problem?

The Climate-KIC report does a nice job of explaining the 5 components
of this solution to the decentralization challenge:

1. Cryptography - public key encryption and hashing functions allows
protecting the privacy, integrity, and even the anonymity of data in
the system. This is familiar technology used in secure websites with
[HTTPS](https://en.wikipedia.org/wiki/HTTPS), for example.
2. [Hash tree](https://en.wikipedia.org/wiki/Merkle_tree) - this is
simply a list of records whose integrity is protected by a
cryptographic hash on each record which combines the hash of the
previous record, a timestamp, and the transaction data. This is a
well-understood concept that is used to good effect in systems like
the [Git Version Control System
(VCS)](https://en.wikipedia.org/wiki/Git).
3. [Peer-to-peer networks](https://en.wikipedia.org/wiki/Peer-to-peer) -
this is allows you to build resilient storage by having peers in a
network replicate data to other peers. Heard of Napster and
Bittorrent?
4. [Consensus](https://en.wikipedia.org/wiki/Consensus_(computer_science))
mechanism - how can you authenticate and validate a transaction
in a peer-to-peer network without appealing to a central authority?
Take a look at the [Byzantine General's
Problem](https://en.wikipedia.org/wiki/Byzantine_fault_tolerance#Byzantine_Generals'_Problem). It's difficult.
5. Sybil control mechanism - how do you protect against an actor in
the system generating a large number of fake identities, known as a
[Sybil attack](https://en.wikipedia.org/wiki/Sybil_attack). This too
is hard. Bitcoin's answer is to make it prohibitively expense to abuse
the system this way, with its "Proof of Work" system known as mining.

The first three components - cryptography, hash trees, and
peer-to-peer networks - are well established, and it would be possible
to use them to build an effective, highly-distributed database with
the aid of a central authority (to e.g. decide who can be trusted to
write to the database).

However, to make that database fully decentralized - especially with
anonymous actors writing to the database - some really difficult
challenges are introduced, and that's where the consensus and Sybil
control mechanisms come in. These are much more challenging problems,
and Blockchain is one relatively recent foray into this area.

*Note - in the report, the "Do you need a Blockchain?" flowchart
highlights the idea of a "Permissioned Blockchain" suitable for a case
where all actors are known but untrusted. That does eliminate some of
the difficult problems in this space, but catering for untrusted
writers is where much of the complexity remains.*

*Note also - the report also references an excellent article called
[The Truth About Smart Contracts by Jimmy
Song](https://medium.com/@jimmysong/the-truth-about-smart-contracts-ae825271811f)
which highlights the challenge with attempting to specify and enforce
the rules of a contract using (potentially buggy) computer code
without allowing for appeals to a central authority to interpret the
"spirit" of the contract. And also the challenges of attempting to
link such decentralized contracts with the physical world.*

## Blockchain Inefficiency

Given the challenges that full decentralization brings, it's not
surprising that Blockchain has some drawbacks. To quote some of the
points that jumped out at me in the Climate-KIC report:

> DLT is a highly inefficient database technology that is up to 1
> million times less efficient than a centralised database, which in
> turn leads to much higher energy consumption and GHG emissions.

Given that we're talking about Blockchain in the context of Climate
Change mitigation, that seems important to consider!

> the trade-off between low energy efficiency and higher levels of
> decentralisation is the key question in the DLT for climate action
> ecosystem and needs to be addressed for each potential DLT solution

Blockchain's inefficiency and higher emissions should be weighed up
against a need for decentralization.

> To determine whether DLT is the right tool to solve a given problem,
> it should be validated that DLT is the only solution to the given
> problem. If DLT is not the only solution, also a more efficient
> centralised database can solve the problem.

In other words, you should only consider Blockchain if you've already
eliminated the possibility that a centralized system could be
sufficient.

A more entertaining take on whether Blockchain is a good fit for your
application, from James Mickens:

<iframe width="560" height="315" src="https://www.youtube.com/embed/15RTC22Z2xI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## How Important is Decentralization To Addressing Climate Change?

This is the key point. As [Kirsten
Dunlop](https://twitter.com/kirstenckic) said in her keynote at the
Climate Innovation Summit:

> We have 12 years to set in place profound structural change in
> almost every system of cause and effect in our society

Are the problems associated with centralized systems truly on the
critical path to effectively addressing the climate change challenge?

The Climate-KIC report says:

> While climate change is a truly global problem, it is well
> recognised that it requires a decentralised, multi-stakeholder,
> bottom-up approach to be solved

And that's hard to argue with! I'm a big proponent of bottom-up
innovation guided by a unifying mission, and certainly such a huge
problem space can't be tackled top-down. Mariana Mazzucato's report on
[Mission-oriented research & innovation in the European
Union](https://publications.europa.eu/en/publication-detail/-/publication/5b2811d1-16be-11e8-9253-01aa75ed71a1/language-en)
looks like an excellent framework. And when it comes to Climate
Change, we are all stakeholders.

But ... does that really imply that the technology platforms we use
must be decentralized? For example, a crowd-funding platform hosted by
a single legal entity can still be effective, without itself being
decentralized. Can a sufficiently high level of trust and transparency
be achieved without fully decentralizing the platform? I believe that
is often the case.

To quote the Climate-KIC report again:

> DLT’s main power lies in decentralisation. It currently is unclear
> how the physical centralised world can be decentralised. [...] As
> many climate action solutions are more valuable when synchronised
> with the physical world, this barrier is a key barrier to overcome.

Decentralization and anonymity brings up some pretty fundamental
questions about how human society is organized. And undoubtedly,
tackling Climate Change effectively is going to require fundamental
changes in our society. As Naomi Klein put it, [This Changes
Everything](https://thischangeseverything.org/the-documentary/).

But are the problems that Blockchain claims to solve really the key
problems getting in the way of effective Climate Change mitigation and
adaptation efforts? Even if they are, are there other "good enough"
solutions without the drawbacks of Blockchain that can be deployed
more rapidly?

What I really worry about here is the danger that Climate Change will
be perceived by some as a smokescreen for people pushing pre-existing
agendas that aren't strictly related to the challenges posed by
Climate Change. To take a more extreme example, how likely are we to
mobilize the sort of action needed if people sense they are also being
asked to buy into Anarchism as a political philosophy?

## Conclusion

There is no doubt that Blockchain is a super interesting technology,
and it has opened the door to exciting advances in some truly
difficult computer science problems.

If you are motivated to explore how technology can be used to move
towards a more decentralized society, by all means you should go down
the Blockchain rabbit hole!

However, if you are primarily motivated to rapidly implement Climate
Change mitigation and adaptation solutions in the real world, I would
suggest that you can safely focus your limited resources on
technologies other than Blockchain.
