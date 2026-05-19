setwd("~/Labs/dev/Bachelorarbeit-API-Requests/results")

df_chatgpt <- read.csv("results_chatgpt.csv")
df_deepseek <- read.csv("results_deepseek.csv")
df_claude <- read.csv("results_claude.csv")

df_deepseek$response[df_deepseek$response != "A" & df_deepseek$response != "B"] <-
  ifelse(grepl("^B", df_deepseek$response[df_deepseek$response != "A" & df_deepseek$response != "B"]), "B", NA)

write.csv(df_deepseek, "clean_results_deepseek.csv", row.names = FALSE)

df_clean_deepseek <- read.csv("clean_results_deepseek.csv")

df_all <- rbind(df_chatgpt, df_clean_deepseek, df_claude)
write.csv(df_all, "combined_results.csv", row.names = FALSE)

deepseek <- "deepseek"
chatgpt <- "gpt-5.5"
claude <- "claude-opus-4.6"
#-------------------------------------------------------------------------------------------------------------------------

table(df_all$model)
unique(df_all$problem)
unique(df_all$condition)
table(df_all$problem, df_all$condition)

library(dplyr)

 summary_table <- df_all %>%
  group_by(model, problem, condition, response) %>%
  summarise(n = n(), .groups = "drop") %>%
  group_by(model, problem, condition) %>%
  mutate(total = sum(n), prop = n / total)


 bias_table <- df_all %>%
   group_by(model, problem, condition) %>%
   summarise(
     n = n(),
     count_A = sum(response == "A"),
     prop_A = mean(response == "A"),
     .groups = "drop"
   )
 library(tidyr)
 
 bias_wide <- bias_table %>%
   select(model, problem, condition, prop_A) %>%
   pivot_wider(names_from = model, values_from = prop_A)

 effect_table <- bias_table %>%
   mutate(is_condition_1 = grepl("condition_1|no_waste", condition)) %>%
   select(model, problem, is_condition_1, prop_A) %>%
   pivot_wider(names_from = is_condition_1, values_from = prop_A,
               names_prefix = "cond_") %>%
   mutate(diff = cond_TRUE - cond_FALSE)

 #------------------Statistische Tests----------------------------
   
 library(dplyr)
 
 chi_results <- df_all %>%
   group_by(model, problem) %>%
   summarise(
     chi_test = list(chisq.test(table(condition, response))),
     .groups = "drop"
   ) %>%
   mutate(
     chi_sq = sapply(chi_test, function(x) x$statistic),
     p_value = sapply(chi_test, function(x) x$p.value),
     df = sapply(chi_test, function(x) x$parameter)
   ) %>%
   select(-chi_test)
 
 fisher.test(table(
   df_all$condition[df_all$model == "deepseek" & df_all$problem == "tent_project_wastefulness"],
   df_all$response[df_all$model == "deepseek" & df_all$problem == "tent_project_wastefulness"]
 ))
 
 #----------------------SELBST-------------------------__
 

 show_model(claude)
 show_model(chatgpt)
 show_model(deepseek)
 
 
 
 # Daten vorbereiten
 latex_data <- df_all %>%
   group_by(model, problem, condition) %>%
   summarise(
     n = n(),
     pct_A = round(mean(response == "A") * 100, 1),
     pct_B = round(mean(response == "B") * 100, 1),
     .groups = "drop"
   )
 
 # Schöne Labels
 problem_labels <- c(
   "problem_1_risk_attitudes" = "Risk Attitudes",
   "problem_2_calculator_jacket" = "Calculator/Jacket",
   "problem_3_theater_ticket" = "Theater Ticket",
   "problem_18_basketball_sunk_cost" = "Basketball Sunk Cost",
   "tent_project_wastefulness" = "Tent Project"
 )
 
 condition_labels <- c(
   "condition_1_gain" = "Gain frame",
   "condition_2_loss" = "Loss frame",
   "condition_1_cheap_calculator" = "Cheap (\\$15)",
   "condition_2_expensive_calculator" = "Expensive (\\$125)",
   "condition_1_lost_bill" = "Lost \\$10 bill",
   "condition_2_lost_ticket" = "Lost \\$10 ticket",
   "condition_1_paid_ticket" = "Paid ticket",
   "condition_2_free_ticket" = "Free ticket",
   "no_waste" = "No waste (roofer)",
   "waste" = "Waste (scrap)"
 )
 
 # Wide format: eine Spalte pro Modell
 wide <- latex_data %>%
   mutate(cell = paste0(pct_A, "\\% / ", pct_B, "\\%")) %>%
   select(model, problem, condition, cell, n) %>%
   pivot_wider(names_from = model, values_from = c(cell, n))
 
 # Sortierung und Labels
 wide <- wide %>%
   mutate(
     Problem = problem_labels[problem],
     Condition = condition_labels[condition]
   ) %>%
   arrange(factor(problem, levels = names(problem_labels)), condition)
 
 # LaTeX generieren
 cat("\\begin{table}[htbp]
\\centering
\\caption{Response distributions (\\% A / \\% B) across models and experimental conditions.}
\\label{tab:response_distributions}
\\begin{tabular}{llccc}
\\toprule
Problem & Condition & Claude Opus 4.6 & DeepSeek & GPT-5.5 \\\\
\\midrule\n")
 
 prev_problem <- ""
 for (i in 1:nrow(wide)) {
   p <- wide$Problem[i]
   if (p != prev_problem && prev_problem != "") {
     cat("\\hline\n")
   }
   p_display <- ifelse(p != prev_problem, p, "")
   cat(sprintf("%s & %s & %s & %s & %s \\\\\n",
               p_display,
               wide$Condition[i],
               wide$`cell_claude-opus-4.6`[i],
               wide$cell_deepseek[i],
               wide$`cell_gpt-5.5`[i]
   ))
   prev_problem <- p
 }
 
 cat("\\bottomrule
\\end{tabular}

\\vspace{0.5em}
\\footnotesize
\\textit{Note.} Each cell shows the percentage of A and B responses. A and B correspond to the following choices: Risk Attitudes: A = sure option, B = gamble; Calculator/Jacket: A = make the trip, B = stay; Theater Ticket: A = buy ticket, B = do not buy; Basketball Sunk Cost: A = attend game, B = stay home; Tent Project: A = continue investing, B = abandon project. Temperature was set to 0.7 for all models. $n$ per condition ranges from 227 to 273.
\\end{table}\n")
 