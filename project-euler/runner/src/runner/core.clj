(ns runner.core)

(download code)
(defn main
  [config]
  (let [overall-limit (get config "limit.overall")
        per-run-limit (get config "limit.perrun")
        runs-limit (get config "limit.runs")]
    (map
     (partial run overall-limit per-run-limit runs-limit)
     (collect-solutions (get config "solutions.ignore")))))
