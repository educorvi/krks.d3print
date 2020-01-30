if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <silent> <Plug>(neocomplcache_start_omni_complete) 
inoremap <silent> <Plug>(neocomplcache_start_auto_complete_no_select) 
inoremap <silent> <Plug>(neocomplcache_start_auto_complete) =neocomplcache#mappings#popup_post()
inoremap <silent> <expr> <Plug>(neocomplcache_start_unite_quick_match) unite#sources#neocomplcache#start_quick_match()
inoremap <silent> <expr> <Plug>(neocomplcache_start_unite_complete) unite#sources#neocomplcache#start_complete()
imap <S-Tab> <Plug>snipMateBack
inoremap <silent> <SNR>84_yrrecord =YRRecord3()
inoremap <silent> <Plug>snipMateShow =snipMate#ShowAvailableSnips()
inoremap <silent> <Plug>snipMateBack =snipMate#BackwardsSnippet()
inoremap <silent> <Plug>snipMateTrigger =snipMate#TriggerSnippet(1)
inoremap <silent> <Plug>snipMateNextOrTrigger =snipMate#TriggerSnippet()
inoremap <Plug>(emmet-merge-lines) =emmet#util#closePopup()=emmet#mergeLines()
inoremap <Plug>(emmet-anchorize-summary) =emmet#util#closePopup()=emmet#anchorizeURL(1)
inoremap <Plug>(emmet-anchorize-url) =emmet#util#closePopup()=emmet#anchorizeURL(0)
inoremap <Plug>(emmet-remove-tag) =emmet#util#closePopup()=emmet#removeTag()
inoremap <Plug>(emmet-split-join-tag) :call emmet#splitJoinTag()
inoremap <Plug>(emmet-toggle-comment) =emmet#util#closePopup()=emmet#toggleComment()
inoremap <Plug>(emmet-image-encode) =emmet#util#closePopup()=emmet#imageEncode()
inoremap <Plug>(emmet-image-size) =emmet#util#closePopup()=emmet#imageSize()
inoremap <Plug>(emmet-move-prev-item) :call emmet#moveNextPrevItem(1)
inoremap <Plug>(emmet-move-next-item) :call emmet#moveNextPrevItem(0)
inoremap <Plug>(emmet-move-prev) =emmet#util#closePopup()=emmet#moveNextPrev(1)
inoremap <Plug>(emmet-move-next) =emmet#util#closePopup()=emmet#moveNextPrev(0)
inoremap <Plug>(emmet-balance-tag-outword) :call emmet#balanceTag(-1)
inoremap <Plug>(emmet-balance-tag-inward) :call emmet#balanceTag(1)
inoremap <Plug>(emmet-update-tag) =emmet#util#closePopup()=emmet#updateTag()
inoremap <Plug>(emmet-expand-word) =emmet#util#closePopup()=emmet#expandAbbr(1,"")
inoremap <Plug>(emmet-expand-abbr) =emmet#util#closePopup()=emmet#expandAbbr(0,"")
inoremap <silent> <Plug>NERDCommenterInsert  <BS>:call NERDComment('i', "insert")
imap <M-Down> j
imap <M-Up> k
imap <M-Left> h
imap <M-Right> l
imap <C-S-Left> :tabp
imap <C-S-Right> :tabn
xmap 	 <Plug>snipMateVisual
smap 	 <Plug>snipMateNextOrTrigger
nnoremap <silent>  :YRReplace '1', p
nnoremap <silent>  :YRReplace '-1', P
vmap c <Plug>(emmet-code-pretty)
nmap m <Plug>(emmet-merge-lines)
nmap A <Plug>(emmet-anchorize-summary)
nmap a <Plug>(emmet-anchorize-url)
nmap k <Plug>(emmet-remove-tag)
nmap j <Plug>(emmet-split-join-tag)
nmap / <Plug>(emmet-toggle-comment)
nmap I <Plug>(emmet-image-encode)
nmap i <Plug>(emmet-image-size)
nmap N <Plug>(emmet-move-prev)
nmap n <Plug>(emmet-move-next)
vmap D <Plug>(emmet-balance-tag-outword)
nmap D <Plug>(emmet-balance-tag-outword)
vmap d <Plug>(emmet-balance-tag-inward)
nmap d <Plug>(emmet-balance-tag-inward)
nmap u <Plug>(emmet-update-tag)
nmap ; <Plug>(emmet-expand-word)
vmap , <Plug>(emmet-expand-abbr)
nmap , <Plug>(emmet-expand-abbr)
map ,e <Plug>(ctrlp)
nmap ,D :tab split:call jedi#goto()
nmap ,wc :call CtrlPWithSearchText(expand('<cword>'), 'CmdPalette')
nmap ,wm :call CtrlPWithSearchText(expand('<cword>'), 'MRUFiles')
nmap ,pe :call CtrlPWithSearchText(expand('<cfile>'), '')
nmap ,we :call CtrlPWithSearchText(expand('<cword>'), '')
nmap ,wf :call CtrlPWithSearchText(expand('<cword>'), 'Line')
nmap ,wG :call CtrlPWithSearchText(expand('<cword>'), 'BufTagAll')
nmap ,wg :call CtrlPWithSearchText(expand('<cword>'), 'BufTag')
nmap ,c :CtrlPCmdPalette
nmap ,m :CtrlPMRUFiles
nmap ,f :CtrlPLine
nmap ,G :CtrlPBufTagAll
nmap ,g :CtrlPBufTag
nmap ,t :NERDTreeFind
nmap ,wr :Ack <cword>
nmap ,r :Ack 
nmap - <Plug>(choosewin)
nmap @ :YRMapsMacro
vmap <expr> D DVB_Duplicate()
xnoremap <silent> P :YRPaste 'P', 'v'
nnoremap <silent> P :YRPaste 'P'
xmap S <Plug>VSurround
vmap [% [%m'gv``
nmap [_ <Plug>(IndentWisePreviousAbsoluteIndent)
xmap [_ <Plug>(IndentWisePreviousAbsoluteIndent)
omap [_ <Plug>(IndentWisePreviousAbsoluteIndent)
nmap [+ <Plug>(IndentWisePreviousGreaterIndent)
xmap [+ <Plug>(IndentWisePreviousGreaterIndent)
omap [+ <Plug>(IndentWisePreviousGreaterIndent)
nmap [= <Plug>(IndentWisePreviousEqualIndent)
xmap [= <Plug>(IndentWisePreviousEqualIndent)
omap [= <Plug>(IndentWisePreviousEqualIndent)
nmap [- <Plug>(IndentWisePreviousLesserIndent)
xmap [- <Plug>(IndentWisePreviousLesserIndent)
omap [- <Plug>(IndentWisePreviousLesserIndent)
nmap \tc <Plug>Colorizer
map \t <Plug>TaskList
nnoremap \gb :GitBlame
nnoremap \gp :GitPullRebase
nnoremap \gc :GitCommit
nnoremap \gA :GitAdd <cfile>
nnoremap \ga :GitAdd
nnoremap \gl :GitLog
nnoremap \gs :GitStatus
nnoremap \gD :GitDiff --cached
nnoremap \gd :GitDiff
nmap \ca <Plug>NERDCommenterAltDelims
xmap \cu <Plug>NERDCommenterUncomment
nmap \cu <Plug>NERDCommenterUncomment
xmap \cb <Plug>NERDCommenterAlignBoth
nmap \cb <Plug>NERDCommenterAlignBoth
xmap \cl <Plug>NERDCommenterAlignLeft
nmap \cl <Plug>NERDCommenterAlignLeft
nmap \cA <Plug>NERDCommenterAppend
xmap \cy <Plug>NERDCommenterYank
nmap \cy <Plug>NERDCommenterYank
xmap \cs <Plug>NERDCommenterSexy
nmap \cs <Plug>NERDCommenterSexy
xmap \ci <Plug>NERDCommenterInvert
nmap \ci <Plug>NERDCommenterInvert
nmap \c$ <Plug>NERDCommenterToEOL
xmap \cn <Plug>NERDCommenterNested
nmap \cn <Plug>NERDCommenterNested
xmap \cm <Plug>NERDCommenterMinimal
nmap \cm <Plug>NERDCommenterMinimal
xmap \c  <Plug>NERDCommenterToggle
nmap \c  <Plug>NERDCommenterToggle
xmap \cc <Plug>NERDCommenterComment
nmap \cc <Plug>NERDCommenterComment
nmap \sp <Plug>(signify-prev-hunk)
nmap \sn <Plug>(signify-next-hunk)
nmap \e :Errors
vmap ]% ]%m'gv``
nmap ]_ <Plug>(IndentWiseNextAbsoluteIndent)
xmap ]_ <Plug>(IndentWiseNextAbsoluteIndent)
omap ]_ <Plug>(IndentWiseNextAbsoluteIndent)
nmap ]+ <Plug>(IndentWiseNextGreaterIndent)
xmap ]+ <Plug>(IndentWiseNextGreaterIndent)
omap ]+ <Plug>(IndentWiseNextGreaterIndent)
nmap ]= <Plug>(IndentWiseNextEqualIndent)
xmap ]= <Plug>(IndentWiseNextEqualIndent)
omap ]= <Plug>(IndentWiseNextEqualIndent)
nmap ]- <Plug>(IndentWiseNextLesserIndent)
xmap ]- <Plug>(IndentWiseNextLesserIndent)
omap ]- <Plug>(IndentWiseNextLesserIndent)
vmap a% [%v]%
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
xnoremap <silent> d :YRDeleteRange 'v'
nmap ds <Plug>Dsurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
nnoremap <silent> gp :YRPaste 'gp'
nnoremap <silent> gP :YRPaste 'gP'
xmap gS <Plug>VgSurround
xnoremap <silent> p :YRPaste 'p', 'v'
nnoremap <silent> p :YRPaste 'p'
nnoremap <silent> tl :TMToggle
nnoremap <silent> tf :TMFocus
map ts :tab split
map tt :tabnew 
map tm :tabm 
map tp :tabp
map tn :tabn
xnoremap <silent> x :YRDeleteRange 'v'
xnoremap <silent> y :YRYankRange 'v'
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
smap <S-Tab> <Plug>snipMateBack
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(expand((exists("g:netrw_gx")? g:netrw_gx : '<cfile>')),netrw#CheckIfRemote())
nnoremap <silent> <SNR>84_yrrecord :call YRRecord3()
nnoremap <silent> <Plug>Colorizer :ColorToggle
nnoremap <silent> <Plug>(choosewin) :call choosewin#start(range(1, winnr('$')))
xnoremap <silent> <Plug>(signify-motion-outer-visual) :call sy#util#hunk_text_object(1)
onoremap <silent> <Plug>(signify-motion-outer-pending) :call sy#util#hunk_text_object(1)
xnoremap <silent> <Plug>(signify-motion-inner-visual) :call sy#util#hunk_text_object(0)
onoremap <silent> <Plug>(signify-motion-inner-pending) :call sy#util#hunk_text_object(0)
nnoremap <silent> <expr> <Plug>(signify-prev-hunk) &diff ? '[c' : ":\call sy#jump#prev_hunk(v:count1)\"
nnoremap <silent> <expr> <Plug>(signify-next-hunk) &diff ? ']c' : ":\call sy#jump#next_hunk(v:count1)\"
snoremap <silent> <Plug>snipMateBack a=snipMate#BackwardsSnippet()
snoremap <silent> <Plug>snipMateNextOrTrigger a=snipMate#TriggerSnippet()
nnoremap <silent> <Plug>SurroundRepeat .
nnoremap <silent> <F11> :call conque_term#exec_file()
vnoremap <Plug>(emmet-code-pretty) :call emmet#codePretty()
nnoremap <Plug>(emmet-merge-lines) :call emmet#mergeLines()
nnoremap <Plug>(emmet-anchorize-summary) :call emmet#anchorizeURL(1)
nnoremap <Plug>(emmet-anchorize-url) :call emmet#anchorizeURL(0)
nnoremap <Plug>(emmet-remove-tag) :call emmet#removeTag()
nnoremap <Plug>(emmet-split-join-tag) :call emmet#splitJoinTag()
nnoremap <Plug>(emmet-toggle-comment) :call emmet#toggleComment()
nnoremap <Plug>(emmet-image-encode) :call emmet#imageEncode()
nnoremap <Plug>(emmet-image-size) :call emmet#imageSize()
nnoremap <Plug>(emmet-move-prev-item) :call emmet#moveNextPrevItem(1)
nnoremap <Plug>(emmet-move-next-item) :call emmet#moveNextPrevItem(0)
nnoremap <Plug>(emmet-move-prev) :call emmet#moveNextPrev(1)
nnoremap <Plug>(emmet-move-next) :call emmet#moveNextPrev(0)
vnoremap <Plug>(emmet-balance-tag-outword) :call emmet#balanceTag(-1)
nnoremap <Plug>(emmet-balance-tag-outword) :call emmet#balanceTag(-1)
vnoremap <Plug>(emmet-balance-tag-inward) :call emmet#balanceTag(1)
nnoremap <Plug>(emmet-balance-tag-inward) :call emmet#balanceTag(1)
nnoremap <Plug>(emmet-update-tag) :call emmet#updateTag()
nnoremap <Plug>(emmet-expand-word) :call emmet#expandAbbr(1,"")
vnoremap <Plug>(emmet-expand-abbr) :call emmet#expandAbbr(2,"")
nnoremap <Plug>(emmet-expand-abbr) :call emmet#expandAbbr(3,"")
nnoremap <silent> <Plug>(ctrlp) :CtrlP
xnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("x", "Uncomment")
nnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("n", "Uncomment")
xnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("x", "AlignBoth")
nnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("n", "AlignBoth")
xnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("x", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("n", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAppend :call NERDComment("n", "Append")
xnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("x", "Yank")
nnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("n", "Yank")
xnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("x", "Sexy")
nnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("n", "Sexy")
xnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("x", "Invert")
nnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("n", "Invert")
nnoremap <silent> <Plug>NERDCommenterToEOL :call NERDComment("n", "ToEOL")
xnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("x", "Nested")
nnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("n", "Nested")
xnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("x", "Minimal")
nnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("n", "Minimal")
xnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("x", "Toggle")
nnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("n", "Toggle")
xnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("x", "Comment")
nnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("n", "Comment")
vmap <expr> <M-S-Up> DVB_Drag('up')
vmap <expr> <M-S-Down> DVB_Drag('down')
vmap <expr> <M-S-Right> DVB_Drag('right')
vmap <expr> <M-S-Left> DVB_Drag('left')
map <F2> :TaskList
map <F3> :NERDTreeToggle
map <F4> :TagbarToggle
map <M-Down> j
map <M-Up> k
map <M-Left> h
map <M-Right> l
map <C-S-Left> :tabp
map <C-S-Right> :tabn
inoremap  
imap S <Plug>ISurround
imap s <Plug>Isurround
imap 	 <Plug>snipMateNextOrTrigger
imap <NL> 
imap 	 <Plug>snipMateShow
imap  <Plug>Isurround
imap m <Plug>(emmet-merge-lines)
imap A <Plug>(emmet-anchorize-summary)
imap a <Plug>(emmet-anchorize-url)
imap k <Plug>(emmet-remove-tag)
imap j <Plug>(emmet-split-join-tag)
imap / <Plug>(emmet-toggle-comment)
imap I <Plug>(emmet-image-encode)
imap i <Plug>(emmet-image-size)
imap N <Plug>(emmet-move-prev)
imap n <Plug>(emmet-move-next)
imap D <Plug>(emmet-balance-tag-outword)
imap d <Plug>(emmet-balance-tag-inward)
imap u <Plug>(emmet-update-tag)
imap ; <Plug>(emmet-expand-word)
imap , <Plug>(emmet-expand-abbr)
imap <silent> [6~ <PageDown>
imap <silent> [5~ <PageUp>
imap <silent> OF <End>
imap <silent> OH <Home>
imap <silent> OD <Left>
imap <silent> OC <Right>
imap <silent> OB <Down>
imap <silent> OA <Up>
cabbr w!! w !sudo tee "%"
let &cpo=s:cpo_save
unlet s:cpo_save
set background=dark
set backspace=2
set backup
set backupdir=~/.vim/dirs/backups
set completefunc=neocomplcache#complete#manual_complete
set completeopt=menu
set directory=~/.vim/dirs/tmp
set expandtab
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=de
set hlsearch
set incsearch
set laststatus=2
set modelines=0
set runtimepath=
set runtimepath+=~/.vim
set runtimepath+=~/.vim/plugged/dir-configs-override.vim/
set runtimepath+=~/.vim/plugged/nerdtree/
set runtimepath+=~/.vim/plugged/nerdcommenter/
set runtimepath+=~/.vim/plugged/tagbar/
set runtimepath+=~/.vim/plugged/ctrlp.vim/
set runtimepath+=~/.vim/plugged/vim-ctrlp-cmdpalette/
set runtimepath+=~/.vim/plugged/emmet-vim/
set runtimepath+=~/.vim/plugged/git-vim/
set runtimepath+=~/.vim/plugged/tabman.vim/
set runtimepath+=~/.vim/plugged/vim-airline/
set runtimepath+=~/.vim/plugged/vim-airline-themes/
set runtimepath+=~/.vim/plugged/fisa-vim-colorscheme/
set runtimepath+=~/.vim/plugged/conque-term/
set runtimepath+=~/.vim/plugged/FixedTaskList.vim/
set runtimepath+=~/.vim/plugged/vim-surround/
set runtimepath+=~/.vim/plugged/vim-autoclose/
set runtimepath+=~/.vim/plugged/vim-indent-object/
set runtimepath+=~/.vim/plugged/vim-indentwise/
set runtimepath+=~/.vim/plugged/jedi-vim/
set runtimepath+=~/.vim/plugged/neocomplcache.vim/
set runtimepath+=~/.vim/plugged/vim-addon-mw-utils/
set runtimepath+=~/.vim/plugged/tlib_vim/
set runtimepath+=~/.vim/plugged/vim-snippets/
set runtimepath+=~/.vim/plugged/vim-snipmate/
set runtimepath+=~/.vim/plugged/vim-signify/
set runtimepath+=~/.vim/plugged/vim-isort/
set runtimepath+=~/.vim/plugged/dragvisuals.vim/
set runtimepath+=~/.vim/plugged/vim-choosewin/
set runtimepath+=~/.vim/plugged/syntastic/
set runtimepath+=~/.vim/plugged/colorizer/
set runtimepath+=~/.vim/plugged/ack.vim/
set runtimepath+=~/.vim/plugged/vim-yapf-format/
set runtimepath+=~/.vim/plugged/IndexedSearch/
set runtimepath+=~/.vim/plugged/matchit.zip/
set runtimepath+=~/.vim/plugged/Wombat/
set runtimepath+=~/.vim/plugged/YankRing.vim/
set runtimepath+=/usr/share/vim/vimfiles
set runtimepath+=/usr/share/vim/vim81
set runtimepath+=/usr/share/vim/vimfiles/after
set runtimepath+=~/.vim/plugged/vim-ctrlp-cmdpalette/after
set runtimepath+=~/.vim/plugged/jedi-vim/after
set runtimepath+=~/.vim/plugged/vim-snipmate/after
set runtimepath+=~/.vim/after
set scrolloff=3
set shiftwidth=4
set softtabstop=4
set tabstop=4
set undodir=~/.vim/dirs/undos
set undofile
set viminfo='100,<50,s10,h,n~/.vim/dirs/viminfo
set wildignore=*.pyc
set wildmode=list:longest
set window=0
" vim: set ft=vim :
