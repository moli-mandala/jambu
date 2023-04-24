<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>

<div style="margin-top: 30px;">
    <h2><span>${h.map_marker_img(request, ctx.language)} ${h.link(request, ctx.language)}</span> ${ctx.name}</h2>
    % if ctx.description:
    <p>
        ${ctx.description | n}
    </p>
    % endif
    % if ctx.etyma:
    <h4>Etymological notes</h4>
    <p>${u.markdown_handle_links(request, ctx.etyma)|n}</p>
    % endif
</div>

<br>

<div style="clear: both; "/>

% if map_ or request.map:
${(map_ or request.map).render()}
% endif

${request.get_datatable('values', h.models.Value, parameter=ctx).render()}