(ns greplin
  (:require clojure.contrib.combinatorics clojure.string))


(defn condition? [numbers]
  (= (reduce + (butlast numbers)) (last numbers)))


(defn candidates [sequence]
  "Simply generate all possible combinations, without trying to be smart"
  (let [limit (count sequence)]
    (loop [length 3 result '()]
      (if (> length limit)
	result
	(recur (inc length) (concat result (clojure.contrib.combinatorics/combinations sequence length)))))))


(def initial-sequence
     (map
      #(Integer/parseInt %)
      (clojure.string/split (slurp "numbers.csv") #", ")))


; maybe mapping to array would speed up things here
(println (count (filter condition? (candidates initial-sequence))))
