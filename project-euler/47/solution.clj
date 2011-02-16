(ns project-euler)


(defn sieve
  ([limit]
     (sieve limit [2 3 5] (sort (concat (range 5 limit 6) (range 7 limit 6)))))
  ([limit primes candidates]
     (let [candidate (first candidates)]
       (if (= candidate nil)
	 primes
	 (if (every? #(not= (mod candidate %) 0) primes)
	   (recur limit (conj primes candidate) (rest candidates))
	   (recur limit primes (rest candidates)))))))


(defn divisible [dividend divisor]
  (= (rem dividend divisor) 0))


(defn solution [limit distinct]
  (let [distinct (int distinct)
	primes (sieve (Math/round (Math/floor (Math/sqrt limit))))]
    (loop [current 1 result []]
      (if (or (= (count result) distinct) (>= current limit))
	result
	(if (= (count (filter #(divisible current %1) primes)) distinct)
	  (recur (inc current) (conj result current))
	  (recur (inc current) []))))))


(println (first (solution 99999999 4)))
