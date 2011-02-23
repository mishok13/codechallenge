(ns greplin)


(defn fib [[previous current]]
  (let [previous (long previous) current (long current)]
    [current (+ previous current)]))


(defn fib-seq []
  (map first (iterate fib [0 1])))


(defn prime?
  "Check if a number is prime"
  [number]
  ; This actually more of a probabilistic approach, but who cares?
  (let [number (long number)
	limit (Math/round (Math/floor (Math/sqrt number)))]
    (every? #(not= (mod number %) 0) (range 2 limit))))


(defn divisors
  "Find a set of prime divisors for a given number"
  [number]
  (let [number (long number)]
    (loop [current number result (set '())]
      (if (= current 1)
	result
	(let [divisor (first (filter #(= (mod current %) 0) (range 2 (inc current))))]
	  (recur (int (/ current divisor)) (conj result divisor)))))))


(defn divisors-recursive
  "Find all divisors of a number recursively
  Usage and result is the same as in loop-ed version"
  ([number] (divisors-recursive number (set '())))
  ([number divisors-seq]
     (let [number (long number)]
       (if (= number 1)
	 divisors-seq
	 (let [divisor (first (filter #(= (mod number %) 0) (range 2 (inc number))))]
	   (recur (int (/ number divisor)) (conj divisors-seq divisor)))))))


(println (reduce + (divisors (inc (first (filter prime? (drop-while #(< % 277000) (fib-seq))))))))
