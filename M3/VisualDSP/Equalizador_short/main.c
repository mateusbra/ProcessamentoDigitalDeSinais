/* programa para testes com arquivos
-- Lendo arquivo de entrada
-- Processa: Executa o filtro Fir
-- Gera arquivo de saida
-- walter 1.0 
*/

#include <stdio.h>
#include <string.h>
#include <cycles.h>



#define NSAMPLES       100

short Coefs[NSAMPLES]={	// Quantizados em 16bits
#include "Coefeq_short.dat"	     
};


extern short proc_alg( short *, short *, int);

int main(int argc,char *argv[])
{
 	cycle_stats_t stats;   
	FILE *fin,*fout;
	short entrada;
	short saida;

  	short Vet_entr[NSAMPLES];
  
	
	int i;
	
	printf("***************************************************************\n");
	printf("* TESTE COM ARQUIVOS					           		      *\n");
	printf("*                                                             *\n");
	printf("***************************************************************\n");
	printf("\n");
	
	
	fin = fopen("..\\..\\sweep.pcm","rb");
//	fin = fopen("..\\imp.pcm","rb");
    	if ((fin)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Entrada\n");
    		return 0;
  	}
    fout = fopen("..\\sai_audio_tst.pcm","wb");
    	if ((fout)==NULL)
  	{
    		printf("\nErro: nao abriu o arquivo de Saida\n");
    		return 0;
  	}
  	
  	CYCLES_INIT(stats);
  	
  	// Inicializa o vetor de coeficientes
  /*	for( i=0; i<tam_media; i++)
  	{
  		Coefs[i] =  32768/tam_media;
  	}	 
*/
	  	
  printf("Processando ...\n ");

  while (fread(&entrada,sizeof(short),1,fin) == 1) 
  {
		Vet_entr[0] = entrada;
		
		CYCLES_START(stats);	
		
		saida = proc_alg( Coefs, Vet_entr, NSAMPLES);

		CYCLES_STOP(stats);
		fwrite(&saida,sizeof(short),1,fout);
	}

    printf("terminado!\n");
		
    
	CYCLES_PRINT(stats);
		fclose(fin);
		fclose(fout);
		
    return 0;
}


