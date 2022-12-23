call plug#begin('-/.vim/plugged')

Plug 'SirVer/ultisnips'
let g:UltiSnipsExpandTrigger="<Tab>"
let g:UltiSnipsJumpforwardTrigger="<Tab>"
let g:UltiSnipsJumpBackwardTrigger="<$-Tab>"
" If you want :UltiSnipEdit to split your window
let g:UltiSnipsEditSplit="vertical"
let g:UltiSnipsSnippetDirectories = ['~/shsheep/development-environment/Snippets']

Plug 'neoclide/coc.nvim', ('branch': 'release'}

Plug 'preservim/nerdtree'

autocmd VimEnter * NERDTree | wincmd p
autocmd VimEnter * Tagbar
" Close Vim if the only window left opened is a NERDTree.
autocmd BufEnter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let NERDTreeWinSize=20

" TagList
" let Tlist_Use_Right_Window=1
" let Tlist_Exit_OnlyWindow=1
" let Tlist_Auto_Open=1
" let Tlist_WinWidth=25
" let Tlist_Auto_Update=1

" Tagbar
let tagbar_ctags_bin='/home/mkdvp/.local/bin/ctags'
let tagbar_sort=0
let tagbar_width=25
let tagbar_autoclose_netrw=1

" Diminactive
hi ColorColumn ctermbg=0 guibg=#eee8d5 
let g:diminactive_use_syntax=0
" autocmd VimEnter * DimInactiveColorcolumnOn
" autocmd VimEnter * DimInactiveOn

Plug 'tpope/vim-fugitive'

" Plug 'vimwiki/vimwiki', {'branch': 'dev'} 
" let g:vimwiki_conceallevel = 0

Plug 'preservim/tagbar'

Plug 'davidhalter/jedi-vim'

" Plug 'mhinz/vim-startity'

" Initialize plugin system
call plug#end()

" function! ExitWhenOnlyNerdTlist()
  " if tabpagenr("$") == 1 && winnr("$") == 2
    " let windowl = bufname(winbufnr(1))
    " let window2 = bufname(winbufnr(2))
    " if (windowl == t:NERDTreeBufName || windowl == "__Tag_List__") && (window2 == t:NERDTreeBufName || window2 == "__Tag_List__")
)     " quitall
    " endif
  " endif
" endfunction
" autocmd WinEnter * call ExitWhenOnlyNerdTlist()

set nocompatible
set backspace=indent,eol,start
set path+=**
set wildmenu
set autoindent
set smartindent
set smarttab
set tabstop=4
set expandtab
set shiftwidth=4
set smartcase
set hlsearch
set number
set ruler
set mouse=a
set syntax=on
set title
set ut=500
set relativenumber
autocmd FileType c set colorcolumn=80
autocmd FileType cpp set colorcolumn=60
autocmd FileType python set colorcolumn=80

colorscheme industry

cabbr csf cs find
cabbr Csf cs find
cabbr CSf cs find
cabbr CSF cs find
cabbr CS cs
cabbr Cs cs
cabbr Lw w
cabbr LW w
cabbr Noh noh
cabbr NOh noh
cabbr Q q
cabbr Q! q!
cabbr Ql q!
cabbr ql q!
cabbr Vs vs
cabbr VS vs
cabbr Set set
cabbr SEt set
cabbr Sp sp
cabbr SP sp
cabbr Sh sh
cabbr SH sh
cabbr Ter term
cabbr Term term
cabbr W w 
cabbr Wq wq 
cabbr WQ wq
cabbr vrc —/shsheep/shsheep.vimrc
cabbr vvrc vi —/shsheep/shsheep.vimrc

" Typical typo
iabbr calss class
iabbr Calss Class
iabbr clinet client
iabbr Clinet Client
iabbr evnet event
iabbr Evnet Event
iabbr FAlse False
iabbr flase false
iabbr FLase False
iabbr initalize initialize
iabbr Initalize Initialize
iabbr instnace instance
iabbr Instnace Instance
iabbr pInstnace pInstance
iabbr subejct subject
iabbr SUbject Subject
iabbr SUBject Subject
iabbr ture true
iabbr Ture True
iabbr TRue True
iabbr THis This
iabbr tiem time
iabbr Tiem Time
iabbr Time Time

nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)
imap <F2> <C-n>
nmap <F3> :DimInactiveOn<CR>
imap <F3> <ESC><F3>i
nmap <F4> :q<CR>
" nmap <F5> :TlistUpdate<CR>:Tlist<CR> 
imap <FS> <ESC><FS>i
nmap <F6> :UltiSnipsEdit<CR>
imap <F6> <ESC><F6>
nmap <F9> ko{<ESC>jo}<ESC>
imap <F9> <ESC><F9>i 
nmap \bn :bn<Cp>
nmap \bp :bp<CR>

inoremap <expr> <CR> pumvisible() ? "\<C-y>" "\<CR>"
inoremap <C-j> <Left>
inoremap <C-k> <Right>
inoremap <C-l> <Del>
" inoremap <C-g> <C-Left> " Why is it so slow?

" Vim command mode arrow, backspace, delete, home, end mappings
cnoremap <C-a> <Home>
cnoremap <C-j> <Left>
cnoremap <C-k> <Right>
cnoremap <C-l> <Del>
" cnoremap <C-g> <C-Left> " Why is it so slow?

" Start Vim at where you lastly worked
au BufReadPost * if line("\"") > 0 && line("\"") <= line("$") I exe "norm g'\"" I endif

" Recognize Pro+C file as C file to use Taglist and syntax highlight without 
" changing /usr/share/vim/vim80/filetype.vim
au BufRead *.pc set filetype=c

" TOPIC: Toggling Comment (via functions)
" FUNCTIONS: for toggle comments
" FUNCTIONS: set comment's prefix character based on filetype
function! SetCommentPrefix()
    let s:commentjrefix = "# "
    if &filetype == "vim"
        let s:commentjrefix = "\" "
    elseif &filetype ==? "c"
               \ || &filetype ==? "h"
               \ || &filetype ==? "cpp" 
               \ || &filetype ==? "hpp"
        let s:comment_prefix = "// "
    elseif &filetype ==? "py"
        let s:comment_prefix = "# "
    endif
endfunction


" FUNCTION: Maki. Hven line into Comment
function! Commenttine(line_number)
    call SetCommentPrefix()

    let cpos = getpos(".") " Remember current cursor position

    call setpos(".", [0, a:line_number, 0, 0]) " move to selected line

    " just insert comment prefix character at the front of given line 
    exec "normal! P.s:comment_prefix

    call setpos(".", cpos) - Restore cursor position
endfunction

" FUNCTION: Uncomment given line
function! UncommentLine(line_number)
    call SetCommentPrefix()

    let cpos = getpos(".") " remember current cursor position

    call setpos(".", [0, a:line_number, B, B]) "move to selected line

    " remove comment prefix charactor
    " !!! use escape() for some languages's prefix eg. C=> "//"
    exec ".s/n.escape(s:comment_prefix, s:comment_prefix[0])."//"

    call setpos(".", cpos) " Restore cursor position ]
endfunction


" FUNCTION: Check given line number if the line is comment
" ARGS: number
" RETURN: : the line is comment, 0: the line is not comment
function! CheckIsComment(line_number)
    " check the line fur given line number is comment
    let sl = getline(a:line_number)
    letc=B
    while c < strlen(sl)
        let d = c + strlen(s:comment_prefix) - 1
        " sl[c] is space or tabe?
        if " \t" =- slit)
        " ignore indentation
        " pass
        elseif sl[(c):(d)J == s:comment_prefix
            return 1
        else
            return 0
        endif
        let c += 1
    endwhile
    return 0
endfunction


" FUNCTION: Toggle line comment
function! ToggleCommentLine()
    call SetCommentPrefix()
    let cl = line(".")
    if ChecklsComment(cl)
        call UncommentLine(c1)
    else
        call CommentLine(cl)
    endif
endfunction


" FUNCTION: Toggle Raw comment
function! ToggleCommentRange()
  call SetCommentPrefix()
  let line_begin = line("'<")
  


# Define colors
C DEFAULT="\[\033(m\I"
C:WHITE="\[\033[1m\]"
C BLACK="\[\033[30m\]"
C_RED="\[\033[31mA"
C GREEN="\[\833[32m\]"
CIYELLOW="\[\033133m\]"
C_BLUE="\[\033134m\l"
C PURPLE="\[\033[35m\]"
C_CYAN="\[\0331.36mA"
C_LIGHTGRAY="\[\033[37m\]"
C_DARKGRAY="\[\033[1;38m\]"
C_LIGHTRED="\[\033[1;31mA"
C LIGHTGREEN="\[\033[1;32m\]"
C_LIGHTYELLOW="\[\033[103mA"
C_LIGHTBLUE="\[\033[1;34m\]"
C_LIGHTPURPLE="\[\03311;35m\I"
C_LIGHTCYAN="\1\033[1;36m\]"
C BG BLACK="\[\033[40m\]"
C_BG_RED="\[\033[41mA"
C_BG GREEN="\1\033[42m\]"
C_BGIYELLOW="\[\033[43m\]"
C BG BLUE="\[\033[44m\]"
C BG PURPLE="\[\033[45mA"
C_BG_CYAN="\[\033[46mA"
CBGLIGHTGRAY="\[\033147m\j"

parse_git_branch() {
   git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1='\[\033[1;32m\][\ue\h W]\[\033[31m\]$(parse_git_branchkn\[\033[1;326\]\$\[\033[M]

stty -ixon

# User specific environment and startup programs
alias cd-="cd - && ls" 
alias cd-="cd && ls"
alias cd..="cd && ls"
alias cd„="cd  && ls"
alias cd....="cd ../.. && ls"
alias cd,,,,="cd ../.. && ls"
alias clang-format="clang-format -style=file"
alias depl="cd -/shsheep/1Deploy"
alias echi="echo"
alias echp="echo"
alias LS="ls"
alias vy="vim -u -/shsheep/shsheep.vimrc"
alias vi="vy"
alias vo="vy"
alias vu="vy"
alias vbp="vy -/shsheep/shsheep.bash_profile"
alias sbp="source -/shsheep/shsheep.bash_profile"
alias cd..="cd .. && ls"
alias cd„="cd .. ls"
alias cd....="cd ../.. && ls"
alias cd,,,,="cd ../.. && ls"
alias clang-fonnat="clang-format -style=file"
alias depl="cd -/shsheepaDeploy"
alias echi="echo"
alias echp="echo"
alias LS="ls"
alias vy="vim -u -/shsheep/shsheep.vimrc"
alias vi="vy"
alias vo="vy"
alias vu="vy"
Was vbp="vy -/shsheep/shsheep.bashprofile"
alias sbp="source -/shsheep/shsheep.bash_profile"
alias ll="is -alF"
alias vrc="-/shsheep/shsheep.vimrc"
alias vvrc="vy -/shsheep/shsheep.vimrc"
alias g++="g++ -std=c++2a"
alias g ="g++"
alias gpp="g++"
alias a="./a.out"
alias mkae="make"
alias amke="make"
alias amek="make"
alias MC="make clean"
alias gd="git diff"
alias gdt="git difftool"
alias gs="git status"
alias grpe="grep"
alias Grep="grep"
alias Grpe="grep"
alias GRep="grep"
alias GRpe="grep"

TMOUT=0
