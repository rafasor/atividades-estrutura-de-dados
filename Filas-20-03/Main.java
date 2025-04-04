import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

// Sistema de Navegação com Pilhas
class Navegador {
    private Stack<String> voltar;
    private Stack<String> avancar;
    private String paginaAtual;
    
    public Navegador() {
        voltar = new Stack<>();
        avancar = new Stack<>();
        paginaAtual = "Página Inicial";
    }
    
    public void acessarPagina(String novaPagina) {
        if (!paginaAtual.isEmpty()) {
            voltar.push(paginaAtual);
        }
        paginaAtual = novaPagina;
        avancar.clear();
        exibirEstado();
    }
    
    public void voltar() {
        if (!voltar.isEmpty()) {
            avancar.push(paginaAtual);
            paginaAtual = voltar.pop();
        }
        exibirEstado();
    }
    
    public void avancar() {
        if (!avancar.isEmpty()) {
            voltar.push(paginaAtual);
            paginaAtual = avancar.pop();
        }
        exibirEstado();
    }
    
    public void exibirEstado() {
        System.out.println("Página Atual: " + paginaAtual);
        System.out.println("Voltar: " + voltar);
        System.out.println("Avançar: " + avancar);
        System.out.println("---------------------------");
    }
}

// Sistema Gerador de Senhas para o Hospital
class GeradorSenhas {
    private Queue<Integer> fila;
    private int contador;
    private LinkedList<Integer> historico;
    
    public GeradorSenhas() {
        fila = new LinkedList<>();
        historico = new LinkedList<>();
        contador = 1;
    }
    
    public void gerarSenha() {
        fila.add(contador);
        System.out.println("Senha gerada: " + contador);
        contador++;
    }
    
    public void chamarProximo() {
        if (!fila.isEmpty()) {
            int chamada = fila.poll();
            historico.add(chamada);
            System.out.println("Chamando senha: " + chamada);
        } else {
            System.out.println("Nenhuma senha na fila.");
        }
    }
    
    public void exibirHistorico() {
        System.out.println("Histórico de chamadas: " + historico);
    }
}

// Testando as funcionalidades
public class Main {
    public static void main(String[] args) {
        // Teste do Navegador
        Navegador navegador = new Navegador();
        navegador.acessarPagina("Google");
        navegador.acessarPagina("YouTube");
        navegador.voltar();
        navegador.voltar();
        navegador.avancar();
        
        // Teste do Gerador de Senhas
        GeradorSenhas hospital = new GeradorSenhas();
        hospital.gerarSenha();
        hospital.gerarSenha();
        hospital.chamarProximo();
        hospital.chamarProximo();
        hospital.exibirHistorico();
    }
}
