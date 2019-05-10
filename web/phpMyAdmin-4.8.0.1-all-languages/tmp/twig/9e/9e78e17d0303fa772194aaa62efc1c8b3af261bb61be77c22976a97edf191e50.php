<?php

/* config/form_display/group_header.twig */
class __TwigTemplate_5a178aaf8b066942c227a79f96ed1c99304c4b228b3178a87e965d17eabaf17e extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        echo "<tr class=\"group-header group-header-";
        echo twig_escape_filter($this->env, ($context["group"] ?? null), "html", null, true);
        echo "\">
    <th colspan=\"";
        // line 2
        echo twig_escape_filter($this->env, ($context["colspan"] ?? null), "html", null, true);
        echo "\">
        ";
        // line 3
        echo twig_escape_filter($this->env, ($context["header_text"] ?? null), "html", null, true);
        echo "
    </th>
</tr>
";
    }

    public function getTemplateName()
    {
        return "config/form_display/group_header.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  28 => 3,  24 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "config/form_display/group_header.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/config/form_display/group_header.twig");
    }
}
