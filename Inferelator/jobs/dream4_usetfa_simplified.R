PARS$input.dir <- 'input/dream4'

PARS$meta.data.file <- 'meta_data.tsv'
PARS$priors.file <- 'gold_standard.tsv'
PARS$gold.standard.file <- 'gold_standard.tsv'

PARS$num.boots <- 1
PARS$cores <- 12

PARS$delT.max <- 110
PARS$delT.min <- 0
PARS$tau <- 45

PARS$perc.tp <- 50 # rep(50, 4)
PARS$perm.tp <- 1 # rep(1, 4)
PARS$perc.fp <- 0 # c(0, 100, 250, 500)
PARS$perm.fp <- 1 # c(1, 5, 5, 5)

PARS$eval.on.subset <- FALSE

PARS$method <- 'BBSR'
PARS$prior.weight <- 1.26

PARS$save.to.dir <- paste('output/dream4', PARS$method, PARS$prior.weight, sep='_')

PARS$use.tfa <- TRUE
