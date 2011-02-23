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


(defn fib [[previous current]]
  (let [previous (long previous) current (long current)]
    [current (+ previous current)]))

(defn fib-seq []
  (map first (iterate fib [0 1])))


(defn prime? [number]
  (let [number (long number)
	limit (Math/round (Math/floor (Math/sqrt number)))]
    (every? #(not= (mod number %) 0) (range 2 limit))))

(defn divisors [number]
  (let [number (long number)]
    (loop [current number result (set '())]
      (if (= current 1)
	result
	(let [divisor (first (filter #(= (mod current %) 0) (range 2 (inc current))))]
	  (recur (int (/ current divisor)) (conj result divisor)))))))

(println (reduce + (divisors (inc (first (filter prime? (drop-while #(< % 277000) (fib-seq))))))))

;; (println (time (prime? 11212)))
