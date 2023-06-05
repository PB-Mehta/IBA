A certain city has two taxi companies: Company A has 80% of the taxis and
Company B has 20% of the taxis. Company A's taxis have a 95% success rate for picking
up passengers on time, while Company B's taxis have a 90% success rate. If a randomly
selected taxi is late, what is the probability that it belongs to Company A?

Using bayes theorem
A=selected taxi is of company A
B=it is late
we have to find a | b
P(A|B) = (P(B|A) * P(A)) / P(B)


P(B|A) = 1-success rate
       = 1-0.95 
       = 0.05   

P(A) is probability of selecting taxi from company A given as 0.8 


P(B) is the probability of taxi being late

P(B) = P(B|A) * P(A) + P(B|~A) * P(~A)
P(B) = (0.05 * 0.8) + (0.10 * 0.2) = 0.04 + 0.02 = 0.06

so 
P(A|B) = (P(B|A) * P(A)) / P(B) = (0.05 * 0.8) / 0.06 = 0.4 / 0.06 ≈ 0.6667

