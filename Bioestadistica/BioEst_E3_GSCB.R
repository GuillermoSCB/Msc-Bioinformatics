
load("/home/wiremu/Desktop/Bioestadística/Clases_BioEst/Bioestadistica-BloqueAMECP.RData")
install.packages("faraway")
library(faraway)
data(amlxray)
attach(amlxray)
str(amlxray)


disease <- factor(as.character(disease,labels=c("1","0")))
sex <- factor(Sex,labels=c("F","M"))
downs <- factor(downs,labels=c("yes","no"))
mray <- factor(Mray,labels=c("yes","no"))
mupray <- factor(MupRay,labels=c("yes","no"))
mlowray <- factor(MlowRay,labels=c("yes","no"))
fray <- factor(Fray,labels=c("yes","no"))
cray <- factor(Cray,labels=c("yes","no"))
cnray <- factor(datos$CnRay,ordered=F,levels=c(1,2,3,4),labels=c("Ninguno", "1 o 2", "3 o 4", "5 o más"))

datos <- data.frame(amlxray)

#Modelo logit inicial
modelo0 <- glm(formula = disease ~ 1, family = "binomial", data = datos); modelo0


#Modelo logit completo
modelo.global <- glm(formula = disease ~ cray + downs + age + fray + mlowray + mray + mupray + sex + cnray, family = binomial, data = datos); modelo.global

#Commparación del modelo global con el modelo nulo
anova(modelo0, modelo.global, test = "Chisq")
#Así, esta signicación del restos de variables en el modelo, también viene establecida p or el P-valor 0.0.000162 del contraste de signicación del conjunto de variables del modelo dado p or el estadístico G del logaritmo de razón de verosimilitudes.


#Anális del Modelo Global
summary(modelo.global)

confint(modelo.global)
exp(modelo.global$coefficients)
exp(confint(modelo.global))

library(ResourceSelection)
hoslem.test(datos$disease, fitted(modelo.global))

 #clasificacion: Matriz de confusion corte=0.5
clasificacion(datos$disease, modelo.global, corte = 0.5)

#Curva ROC del Modelo Global
install.packages("Epi")
library(Epi)
curva.modelo.global <- ROC(form=disease ~ . -ID, plot="ROC",PV=T,MX=T,AUC=T,data=datos)

#clasificacion: Matriz de confusion corte=lo que diga ROC
clasificacion(datos$disease, modelo.global, corte = 0.513)

#Selección y análisis del modelo ajustado
modelo.stepAIC <- step(modelo0,scope=list(lower=modelo0,upper=modelo.global),direction="both")

anova(modelo.stepAIC, test="Chisq")

hoslem.test(datos$disease, fitted(modelo.stepAIC))

curva.modelo.stepeAIC <- ROC(form=disease ~ fray + mupray + cnray + downs, plot="ROC",PV=T,MX=T,AUC=T,data=datos)

clasificacion(datos$disease, modelo.stepAIC, corte = 0.416)
