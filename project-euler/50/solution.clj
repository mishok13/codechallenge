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


(defn prime? [number primes]
  (every? #(not= (mod number %) 0) (take-while #(<= % (/ number 2)) primes)))


(prime? 17 [2 3 5 7 11 13])


(defn slice [seq start stop]
  (loop [current start result []]
    (if (>= current stop)
      result
      (recur (inc current) (conj result (nth seq current))))))


(defn consequtives [conseq limit]
  (let [primes (sieve (* (int (/ limit conseq)) 3))
	conseq (int conseq)]
    (first
     (filter
      #(prime? (reduce + %) primes)
      (take-while #(<= (reduce + %) limit)
		  (map #(slice primes %1 (+ %1 conseq))
		       (range 0 (- (count primes) conseq))))))))

(defn solution [limit]
  (loop [conseq (int (Math/round (Math/sqrt limit)))]
    (let [result (consequtives conseq limit)]
      (if (not-empty result)
	result
	(recur (dec conseq))))))

(def result (solution 1000000))
(println result)
(println (reduce + result))


;; (time (count (sieve 50000)))
;; (time (count (set (sieve 50000))))
;; (time (count (set (sieve 1000000))))
