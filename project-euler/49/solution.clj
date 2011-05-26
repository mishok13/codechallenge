(ns project-euler
  (:use clojure.contrib.combinatorics))


(println (combinations (range 1 4) 2))


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


(defn prime?
  ([number]
     (let [number (int number)]
       (prime? number (set (sieve (inc number))))))
  ([number primes]
     (let [number (int number)]
       (every? #(not= (mod number %) 0) primes))))


(defn condition?
  [numbers]
  (let [numbers (sort numbers)]
    (if (not= (count numbers) 3)
      false
      (= (- (second numbers) (first numbers))
	 (- (second (rest numbers)) (second numbers))))))


(defn number-permutations [number]
  (map #(Integer/parseInt (apply str %)) (permutations number)))

(defn prime-permutations [primes number]
  (set (filter #(and (contains? primes %) (> % 1000)) (number-permutations number))))

(defn primes-permutated [primes primes-cache]
  (map #(prime-permutations primes-cache %) (map sort (set (map sort (map str primes))))))

(defn primes-permutated-and-counted [primes primes-cache]
  (map sort (map set (filter #(>= (count %) 3) (primes-permutated primes primes-cache)))))

(println (combinations '(1487 1847 4817) 3))

(defn solve []
  (let [primes (drop-while #(< % 1000) (sieve 10000))
	primes-cache (set (sieve 10000))]
    (map #(filter condition? (combinations % 3)) (primes-permutated-and-counted primes primes-cache))))
(println (solve))




;; (println (filter prime? (map #(Integer/parseInt (apply str %)) (lex-permutations '(1 3 5 7)))))

;; (println (set (map sort (map str (drop-while #(< % 1000) (sieve 10000))))))
;; (println (count (set (map str (drop-while #(< % 1000) (sieve 10000))))))
