/* Implementação de um filtro FIR 
Lê um arquivo binário com amostras em 16bits
Salva arquivo filtrado também em 16 bits
Walter versão 1.0 
 */
#include <stdio.h>
//#include <fcntl.h>
//#include <io.h>
#include <cycles.h>


#define NSAMPLES       100

int main()
{
  	cycle_stats_t stats;
	FILE *in_file, *out_file;
   int i, n, n_amost;
   float GA,GF,GB;
   short entrada, saida;
	   short sample[NSAMPLES] = {0x0};

   float y=0;

   
	float coefPA[NSAMPLES]={
   				#include "CoefPA.dat"
   };
  
 	float coefPB[NSAMPLES]={
   				#include "CoefPB.dat"
   };
   	float coefPF[NSAMPLES]={
   				#include "CoefPF.dat"
   };
   
   float coef[NSAMPLES];
   GB = 0.8;
   GF = 0.5;
   GA = 0.1;
   for(i=0;i<NSAMPLES;i++){
   		coef[i] = coefPB[i]*GB + coefPF[i]*GF + coefPA[i]*GA;
   }
  // inicializando a estrutura de cycles
  CYCLES_INIT(stats);
   /* abre os arquivos de entrada e saida */
  if ((in_file = fopen("..//..//sweep.pcm","rb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de entrada\n");
    return 0;
  }
  if ((out_file = fopen("..//sai_sweep_Eq.pcm","wb"))==NULL)
  {
    printf("\nErro: Nao abriu o arquivo de saida\n");
    return 0;
  }

   // zera vetor de amostras
   for (i=0; i<NSAMPLES; i++)
        {
        sample[i]=0;
        }

   // execução do filtro
 do {
        
 		
	   //zera saída do filtro
        y=0;

        //lê dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
		CYCLES_START(stats);
        sample[0] = entrada;

        //Convolução e acumulação
        for (n=0; n<NSAMPLES; n++)
                {
                y += coef[n]*sample[n];
                }

        //desloca amostra
        for (n=NSAMPLES-1; n>0; n--)
                {
                sample[n]=sample[n-1];
                }

		saida = (short) y;
		CYCLES_STOP(stats);

        //escreve no arquivo de saída
        fwrite(&saida,sizeof(short),1,out_file);

 } while (n_amost);
 
 	CYCLES_PRINT(stats);


   //fecha os arquivos de entrada de saída
   fclose(out_file);
   fclose(in_file);
   return 0;
}
