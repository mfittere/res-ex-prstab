# Cartoon of steady-state beam density given the diffusion coefficient
# illustrating the effect of the hollow electron beam collimator

# amplitudes of various elements
# aperture [beam sigmas]
Jm = 0; JM = 9
# collimator
Jc = 6; Jc2 = JM
# hollow electron beam
Jh = 4; Jh2 = 7

# smooth "hat" function, 0-1-0
hat = function(x
               , x1=0 # starting point
               , x2=1 # end point
               , s=0.05 # width of transition
               ) {
  return(pnorm(x, mean=x1, sd=s) - pnorm(x, mean=x2, sd=s)) }

# shapes of diffusion coefficient vs. amplitude
# power law
D.pow = function(J # amplitude
                 , D0=1e-2 # diffusion coeff. at zero amplitude
                 , Dc=1 # diffusion coeff. at collimator
                 , P=4 # power
                 , Jlim=1 # amplitude at which diffusion coeff. starts to grow
                 , HEBC=FALSE # hollow electron beam on?
                 , hbs=3 # diffusion amplification due to hollow beam
                 ) {
  D = D0+0*J
  sub = Jlim < J & J <= Jc
  D[sub] = D0 + (Dc-D0)*((J[sub]-Jlim)/(Jc-Jlim))^P
  if(HEBC) D = D + Dc*hat(J, Jh, Jh2)*hbs
  sub = Jc < J
  D[sub] = NA
  return(D)
}
# empirical form, Gaussian + power tail beam distribution
D.test = function(J # amplitude
                  , Nc=1 # relative core population
                  , Nh=1/3 # relative halo population
                  , P=2 # power
                  , HEBC=FALSE # hollow electron beam on?
                  , hbs=2 # diffusion amplification due to hollow beam
                  ) {
  D = J / (Nc*J*exp(-0.5*J^2)/sqrt(2*pi) + P*(P+1)*Nh*(2*Jc-J)^(P-1)/Jc^(P+1))
  if(HEBC) D = D*(1 + hbs*hat(J, Jh, Jh2))
  sub = Jc < J
  D[sub] = NA
  return(D)
}
# choose which form to use
D = D.pow

# calculation of gradient and distribution from diffusion coefficient
df = function(J, k=1, HEBC=FALSE){ k*J/D(J, HEBC=HEBC) }

f = f.calc = function(J, HEBC=FALSE){
  I = 0*J
  for(i in 1:length(J)){
    if(J[i]<Jc) I[i] = integrate(df, J[i], Jc, HEBC=HEBC)$value }
  return(I)}

# plot setup
wi = 3.25; he = 3.25; pt = 10; fo = 'Times'
pdf(file='tmp-diffusion.pdf', width=wi, height=he, pointsize=pt, family=fo)
par(oma=rep(0,4), mar=c(3.2,2.2,0.2,2.2))

plot(c(Jm, JM), c(0,1), type='n', axes=FALSE, xlab='', ylab='')

# hollow electron beam
colH = rgb(254, 209, 65, names='prairiegold', maxColorValue=255)
# colH = 'lightgray'
rect(Jh, 0, Jh2, 1, col=colH, border=NA)

# collimator
colC = 'darkgray'
rect(Jc, 0, Jc2, 1, col=colC, border=NA)

# plot curves with hollow beam off and on
for(hb in c(FALSE, TRUE)) {

# particle density
#colF = rgb(0, 76, 151, names='nalblue', maxColorValue=255)
#colF = rgb(0, 40, 85, names='nalbluedark', maxColorValue=255)
#colF = 'darkblue'
colF = 'black'
if(hb) ltyF = 'dashed' else ltyF = 'solid'
plot.window(c(Jm, JM), c(0, f(Jm, HEBC=hb)))
curve( f(x, HEBC=hb), Jm, JM, lwd=2, col=colF, lty=ltyF, add=TRUE)
mtext(expression(paste('Beam population density, ', italic(f(x, t)))), side=2,
      line=1, col=colF)

# diffusion coefficient
colD = rgb(203, 96, 21, names='orange', maxColorValue=255)
#colD = rgb(175, 39, 47, names='masseyfergusonredlight', maxColorValue=255)
#colD = rgb(120, 190, 32, names='nalgreenlight', maxColorValue=255)
#colD = rgb(76, 140, 43, names='nalgreen', maxColorValue=255)
#colD = 'magenta'
if(hb) ltyD = 'dashed' else ltyD = 'solid'
plot.window(c(Jm, JM), c(0, D(Jc, HEBC=TRUE)))
curve( D(x, HEBC=hb), Jm, Jc, lwd=2, col=colD, lty=ltyD, add=TRUE)
mtext(expression(paste('Diffusion coefficient, ', italic(D(x)))), side=4,
      line=1, col=colD)

}

# legends
plot.window(c(Jm, JM), c(0,1))
text(0.5*(Jc+Jc2), 0.5, 'COLLIMATOR', srt=90, font=1)
text(0.5*(Jh+Jc), 0.5, 'HOLLOW ELECTRON BEAM', srt=90, font=1)

# horizontal axis
mtext(expression(paste('Transverse position, ', italic(x), ' [', italic(sigma), ']',
    sep='')), side=1, line=2)
box(); axis(1)

dev.off()
