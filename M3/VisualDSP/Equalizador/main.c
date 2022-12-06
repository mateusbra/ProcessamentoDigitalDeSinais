/* Implementa��o de um filtro FIR 
L� um arquivo bin�rio com amostras em 16bits
Salva arquivo filtrado tamb�m em 16 bits
Walter vers�o 1.0 
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
  
   short entrada, saida;
	   short sample[NSAMPLES] = {0x0};

   float y=0;

   
	float coef[NSAMPLES]={
   				#include "CoefEq.dat"
   };
  
 
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

   // execu��o do filtro
 do {
        
 		
	   //zera sa�da do filtro
        y=0;

        //l� dado do arquivo
        n_amost = fread(&entrada,sizeof(short),1,in_file);
		CYCLES_START(stats);
        sample[0] = entrada;

        //Convolu��o e acumula��o
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

        //escreve no arquivo de sa�da
        fwrite(&saida,sizeof(short),1,out_file);

 } while (n_amost);
 
 	CYCLES_PRINT(stats);


   //fecha os arquivos de entrada de sa�da
   fclose(out_file);
   fclose(in_file);
   return 0;
}
