(defn sieve
  ([limit]
     (sieve limit [2 3 5] (sort (concat (range 5 limit 6) (range 7 limit 6)))))
  ([limit primes candidates]
     (let [candidate (first candidates)
	   limit (int limit)]
       (if (= candidate nil)
	 primes
	 (if (every? #(not= (mod candidate %) 0) primes)
	   (recur limit (conj primes candidate) (rest candidates))
	   (recur limit primes (rest candidates)))))))


(defn solve [limit]
  (let [limit (int limit)
	primes (sieve limit)
	primes-cache (set primes)
	twice-a-square (map #(* 2 % %) (range 1 limit))
	odds (filter #(not (contains? primes-cache %)) (range 5 limit 2))]
    (loop [current (first odds) odds (rest odds)]
      (if (every? #(not (contains? primes-cache (- current %))) twice-a-square)
	current
	(recur (first odds) (rest odds))))))

(println (time (solve 10000)))
