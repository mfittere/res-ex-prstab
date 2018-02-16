# Cartoon of steady-state beam density
# given the diffusion coefficient

for(HEBC in c(FALSE, TRUE)) {

# aperture [beam sigmas]
Jm <- 0; JM <- 9

# collimator
Jc <- 6; Jc2 <- JM

# hollow electron beam
Jh <- 4; Jh2 <- 7

# diffusion coefficient
hat <- function(x, x1=0, x2=1, s=0.1) {
  return(pnorm(x, mean=x1, sd=s) - pnorm(x, mean=x2, sd=s)) }

D.pow <- function(J, D0=0.01, Dc=0.5, P=2) {
 D <- D0 + (Dc-D0)*(J/Jc)^P
 if(HEBC) D <- D + Dc*hat(J, Jh, Jh2)
 sub <- Jc < J
 D[sub] <- NA
 return(D)
}

D.test <- function(J, Nc=1, Nh=1/3, P=2) {
 D <- J / (Nc*J*exp(-0.5*J^2)/sqrt(2*pi) + P*(P+1)*Nh*(2*Jc-J)^(P-1)/Jc^(P+1))
 if(HEBC) D <- D*(1 + 2*hat(J, Jh, Jh2))
 sub <- Jc < J
 D[sub] <- NA
 return(D)
}

D <- D.test

# calculation of gradient and distribution
df <- function(J, k=1){ k*J/D(J) }
f.calc <- function(J){
  I <- 0*J
  for(i in 1:length(J)){
    if(J[i]<Jc) I[i] <- integrate(df, J[i], Jc)$value }
  return(I)}

f.test <- function(J){
    I <- 0*J
    subset <- abs(J)<Jc
    Nc <- 1; Nh <- 1; P <- 1
    if(HEBC){ Nc <- 1.7; Nh <- 0.3 }
    I[subset] <- Nc*exp(-0.5*J[subset]^2)/sqrt(2*pi) +
        Nh*(P+1)*(Jc-J[subset])^P/Jc^(P+1)
    return(I) }

f <- f.calc

# plot setup
wi <- 3.25; he <- 3.25; pt <- 10; fo <- "Times"
dev.new(width=wi, height=he, pointsize=pt, family=fo)
par(oma=rep(0,4), mar=c(3.2,2.2,0.2,2.2))
#    bg="cornsilk")

plot(c(Jm, JM), c(0,1), type="n", axes=FALSE,
     xlab="", ylab="")

# hollow electron beam
colH <- "orange2"
if(HEBC){
  rect(Jh, 0, Jh2, 1, col=colH, border=NA)
}

# collimator
colC <- "darkgray"
rect(Jc, 0, Jc2, 1, col=colC, border=NA)

# particle density
colF <- "#000066"
plot.window(c(Jm, JM), c(0, f(Jm)))
curve( f(x), Jm, JM, lwd=3, col=colF, add=TRUE)
mtext(expression(paste("Beam population density, ", f(x, t))), side=2,
      line=1, col=colF)

# diffusion coefficient
colD <- "green4"
#plot.window(c(Jm, JM), c(D(Jm), D(Jc)))
#plot.window(c(Jm, JM), c(0, D(Jc)))
plot.window(c(Jm, JM), c(0, 340))
curve( D(x), Jm, Jc, lwd=3, col=colD, add=TRUE)
mtext(expression(paste("Diffusion coefficient, ", D(x))), side=4,
      line=1, col=colD)

# legends
plot.window(c(Jm, JM), c(0,1))
text(0.5*(Jc+Jc2), 0.5, "COLLIMATOR", srt=90, font=2)
if(HEBC) text(0.5*(Jh+Jc), 0.5, "HOLLOW ELECTRON BEAM", srt=90, font=2)

# horizontal axis
mtext(expression(paste("Transverse position, ", x, " [", sigma, "]",
    sep="")), side=1, line=2)
box(); axis(1)

# print
fn <- "tmp_diff_off"
if(HEBC) fn <- "tmp_diff_on"
dev.print(pdf, file=paste(fn, "pdf", sep="."), width=wi, height=he,
          pointsize=pt, family=fo)
dev.copy2eps(file=paste(fn, "eps", sep="."), width=wi, height=he,
             pointsize=pt, family=fo)

}
