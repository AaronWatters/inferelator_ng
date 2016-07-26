# commands to install needed R packages

install.packages('inline', repos='http://cran.us.r-project.org')
install.packages('parallel', repos='http://cran.us.r-project.org')
#install.packages('corpcor', repos='http://cran.us.r-project.org') -- doesn't work on travis
install.packages("corpcor", dependencies=TRUE, repos='http://cran.rstudio.com/')
# This doesn't work on travis:
# install.packages('ggplot2', repos='http://cran.us.r-project.org')
